from sqlite3 import Cursor
import pymongo
from pprint import pprint

DATABASE = 'opendata'
COLLECTION = 'AQI'

client = pymongo.MongoClient()
db = client[DATABASE]

Cursor = db.avgaqi.find()

pprint(list(Cursor))