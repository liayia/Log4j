import pymongo
from pprint import pprint

DATABASE = 'opendata'
COLLECTION = 'AQI'

client = pymongo.MongoClient()
db = client[DATABASE]

Cursor = db.geoAQI.find({
    'geometry': {
        '$geoWithin': {
            '$box': [

          [
            121.13937377929688,
            24.877715777296856
          ],
          [
            121.35498046875,
            24.986058021167594
          ]

            ]
        }
    }
}, {'County': 1, 'SiteName': 1, 'AQI': 1, '_id': 0})

pprint(list(Cursor))