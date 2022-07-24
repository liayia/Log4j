import pymongo
from pprint import pprint

DATABASE = 'turist'
COLLECTION = 'spot'

client = pymongo.MongoClient()
db = client[DATABASE]

Cursor = db.spot.find({
    'geometry': {
        '$geoWithin': {
            '$polygon': [
                
            [
              121.33232116699217,
              25.027750592082853
            ],
            [
              121.14898681640626,
              24.972364838003802
            ],
            [
              121.32888793945312,
              24.958670130576788
            ],
            [
              121.40510559082031,
              24.889550882114328
            ],
            [
              121.46965026855469,
              25.05761119143144
            ],
            [
              121.33232116699217,
              25.027750592082853
            ]
            
            ]        
        }
    }
}, {'Name': 1, 'Description': 1, 'Add': 1, '_id': 0})

pprint(list(Cursor))