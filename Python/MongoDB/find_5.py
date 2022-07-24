import pymongo
from pprint import pprint

#DATABASE = 'test'
#COLLECTION = 'taiwan'

client = pymongo.MongoClient()
#db = client[DATABASE]
db = client.test

Cursor = db.taiwan.find({
    'geometry': {
        '$geoIntersects': {
            '$geometry': {
                'type': 'Point',
                'coordinates': [
                    121.21696472167969,
                    24.9648951865082
                ]
            }
        }
    }
}, {'County': 1, '_id': 0})

pprint(list(Cursor))