import requests

import db.configure as DB
import caseStatus as CaseStatus

# MAIN
def main():
  serviceCentersCollection = DB.database["service_centers"]
  result = serviceCentersCollection.find({ "active" : True }, {'_id': 0, 'code': 1, 'last_number': 1})
  for record in result:
    CaseStatus.getStatusForReceiptNumber(record['code'], record['last_number'])
  return

main()
