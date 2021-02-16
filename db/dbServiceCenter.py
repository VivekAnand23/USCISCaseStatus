import datetime
from .configure import database as DB

def insert_doc(doc):
    doc['_id'] = str(db.seqs.find_and_modify(
        query={ 'collection' : 'admin_collection' },
        update={'$inc': {'id': 1}},
        fields={'id': 1, '_id': 0},
        new=True
    ).get('id'))

    try:
        db.admin_collection.insert(doc)

    except pymongo.errors.DuplicateKeyError as e:
        insert_doc(doc)

def insertReceiptStatus(record):
  # Store receipt number
  receipt = DB['receipt']

  receipt.update(
    { 'number': record[0], 'form': record[1] },
    {'number': record[0], 'form': record[1]},
    upsert=True
  )

  # Find the receipt for Receipt Number and Form
  result = receipt.find_one({ 'number': record[0], 'form': record[1] }, { '_id': 1 })

  # Store Status against receipt number
  status = DB['status']
  statusChangedOn = datetime.datetime.strptime(record[3], '%B %d, %Y')
  statusRecord = { 'receipt_id': result['_id'], 'detail': record[2], 'on': statusChangedOn }
  status.update(
    statusRecord,
    statusRecord,
    upsert=True
  )

  return

def getReceiptSequence(sequence_name):
  sequence = DB['sequence']
  updated_record = sequence.find_one_and_update(
    filter={"_id": sequence_name},
    upsert=True,
    update={"$inc": {"sequence_value": 1}},
    return_document=True)
  return f"{updated_record['sequence_value']}"

def printRecords():
  docs = DB.receipt.aggregate(
    [
      {
        "$lookup":{
          "from": "status",       # other table name
          "localField": "_id",        # key field in collection 2
          "foreignField": "receipt_id",      # key field in collection 1
          "as": "linked_collections"   # alias for resulting table
        }
      }
    ]
  )
  for doc in docs:
    print(doc)