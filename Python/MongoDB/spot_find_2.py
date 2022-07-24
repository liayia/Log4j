import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.turist

Cursor = db.spot.find({
    'geometry': {
        '$geoWithin': {
            '$centerSphere': [[121.47583007812501,25.014062054764015],
            50 / 6378.1
            ]        
        }
    }
}, {'Name': 1, 'Description': 1, 'Add': 1, '_id': 0})

pprint(list(Cursor))