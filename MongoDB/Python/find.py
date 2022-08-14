import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata
docs = db.AQI.find()

pprint(list(docs))
