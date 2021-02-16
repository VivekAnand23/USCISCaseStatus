Run following commands:

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

This code only runs for SRC and MSC centers. Please replace the Code with your own.

Update the following constants in code:

1. **NUMBER_OF_RECORDS** = [_Number of receipts to check for_]
2. **DATABASE** = USCIS

Call either srcApplications() or mscApplications()

Run using following command

```
python caseStatus.py
```

## MongoDB

https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-os-x/

1. https://www.mongodb.com/try/download/enterprise?tck=docs_server
2. tar -zxvf mongodb-macos-x86_64-enterprise-4.4.3.tgz
3. Ensure the binaries are in a directory listed in your PATH environment variable.
   sudo cp /path/to/the/mongodb-directory/bin/_ /usr/local/bin/
   sudo ln -s /path/to/the/mongodb-directory/bin/_ /usr/local/bin/
4. Create the data directory. (~/Database/data/db)
5. Create the log directory. (sudo mkdir -p /usr/local/var/log/mongodb)
6. Run MongoDB. (mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork)
7. Verify that MongoDB has started successfully. (ps aux | grep -v grep | grep mongod)
8. Begin using MongoDB. (mongo)

# DB Master data

### Collection `service_centers`

```json
{ _id: ObjectId("601e241002579e2cba0d6721"), code: 'SRC', name: 'Texas Service Center', last_number: 2190128030, active: false }
{ _id: ObjectId("601e241002579e2cba0d6722"), code: 'LIN', name: 'Nebraska Service Center', last_number: 2190183615, active: false }
{ _id: ObjectId("601e241002579e2cba0d6723"), code: 'MSC', name: 'National Benefits Center', last_number: 2190791623, active: true }
{ _id: ObjectId("601e241002579e2cba0d6724"), code: 'CSC', name: 'California Service Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d6725"), code: 'EAC', name: 'Vermont Service Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d6726"), code: 'IOE', name: 'ELIS (e-Filing) Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d6727"), code: 'NBC', name: 'National Benefits Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d6728"), code: 'NSC', name: 'Nebraska Service Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d6729"), code: 'TSC', name: 'Texas Service Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d672a"), code: 'VSC', name: 'Vermont Service Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d672b"), code: 'WAC', name: 'California Service Center', last_number: 2190107297, active: false }
{ _id: ObjectId("601e241002579e2cba0d672c"), code: 'YSC', name: 'Potomac Service Center', last_number: 2190107297, active: false }
```
