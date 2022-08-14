import pymongo
import random

client = pymongo.MongoClient(['localhost:27017', 'localhost:27018'])
db = client.test

# 刪除資料表d
db.d.drop()
# 設定索引與片鍵
db.d.create_index('lv')
db.d.create_index('n')
client.admin.command('shardCollection', 'test.d', key={'lv': 1})

# 插入資料
num = 480000
for i in range(100):
    db.d.insert_one({
        'lv': random.choice('ABCDE'),
        'n': random.randint(1, 50),
        'junk': '_' * num
    })
    print(i)