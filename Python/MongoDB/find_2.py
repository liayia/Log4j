import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata
docs = db.AQI.find({}, {"County":1 , "SiteName": 1 , "AQI": 1})

pprint(list(docs))
