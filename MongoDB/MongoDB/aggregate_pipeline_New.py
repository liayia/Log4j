import pymongo
from pprint import pprint

DATABASE = 'opendata'
COLLECTION = 'AQI'

client = pymongo.MongoClient()
db = client[DATABASE]

pipeline = []

docs = db.AQI.aggregate(pipeline)
pprint(list(docs))
