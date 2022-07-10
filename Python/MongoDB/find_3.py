import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client.opendata
#docs = db.AQI.find({}, {"County":1 , "SiteName": 1 , "AQI": 1})

# 排序 - 依筆劃(反向)
#docs = db.AQI.find(
#    {},
#    {'SiteName': 1 , 'AQI': 1 , '_id': 0 }
#).collation({'locale':'zh_Hant'})sort('SiteName', -1)

# 查詢 AQI >= 40 資料 , 並由小到大排序
#docs = db.AQI.find(
#    {'AQI': {'$regex' : '[4-9].|[1-9]..'}},
#    {'County':1,'SiteName':1,'AQI':1,'_id':0}
#).collation({'locale':'zh_Hant'})sort('SiteName')

# 更新一筆 $set , 如果找不到資料就新增
db.AQWI.updateOne(
    {name: 'May'},
    {'$set': {age: 50}}, 
    upsert=True
)

pprint(list(docs))
