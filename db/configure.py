import pymongo
import configurationParser as CP

# Connect to MongoDB
mongoClient = pymongo.MongoClient(
  "mongodb://" +
  CP.properties['DEFAULT']["HOST"] + ":" +
  CP.properties['DEFAULT']["PORT"] + "/")
database = mongoClient[CP.properties['DEFAULT']["DATABASE"]]
