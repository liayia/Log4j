import pymongo
from pprint import pprint

DATABASE = 'opendata'
COLLECTION = 'AQI'

client = pymongo.MongoClient()
db = client[DATABASE]

pipeline = [
    {
        '$project': {
            '_id': 0, 
            'SiteName': 1, 
            'County': 1, 
            'AQI': 1, 
            'Status': 1
        }
    }, {
        '$addFields': {
            'iAQI': {
                '$toInt': '$AQI'
            }
        }
    }, {
        '$group': {
            '_id': '$County', 
            'AverageAQI': {
                '$avg': '$iAQI'
            }
        }
    }, {
        '$addFields': {
            'tmp': {
                '$round': [
                    '$AverageAQI', 0
                ]
            }
        }
    }, {
        '$sort': {
            'AverageAQI': -1
        }
    }, {
        '$limit': 3
    }
]

docs = db[COLLECTION].aggregate(pipeline)
pprint(list(docs))