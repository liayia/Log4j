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
            [121.21696472167969,24.9648951865082],
            10 / 6378.1
        ]


        }
    }
}, {'County': 1, 'SiteName': 1, 'AQI': 1, '_id': 0})

pprint(list(Cursor))