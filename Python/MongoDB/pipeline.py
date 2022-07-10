import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata

pipeline = [
    {
        '$project': {
            '_id': 0, 
            'SiteName': 1, 
            'County': 1, 
            'AQI': 1, 
            'Status': 1, 
            'iAQI': 1
        }
    }, {
        '$addFields': {
            'iAQI': {
                '$toInt': '$AQI'
            }
        }
    }, {
        '$match': {
            'iAQI': {
                '$gte': 40
            }
        }
    }, {
        '$sort': {
            'iAQI': -1
        }
    }
]

docs = db.AQI.aggregate(pipeline)
pprint(list(docs))