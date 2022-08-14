import pymongo
from pprint import pprint

DATABASE = 'opendata'
COLLECTION = 'AQI'

client = pymongo.MongoClient()
db = client[DATABASE]

Cursor = db.geoAQI.find({
    'geometry': {
        '$geoIntersects': {
        '$centerSphere': [



        ]


        }
    }
}, {'County': 1, 'SiteName': 1, 'AQI': 1, '_id': 0})

pprint(list(Cursor))