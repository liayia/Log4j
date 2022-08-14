import pymongo
from pprint import *

client = pymongo.MongoClient('localhost:20000')
db = client.test

cursor = db.members.watch()
print('變化流初始的resume token:: \n{}\n'.format(cursor.resume_token))
while True:
    document = next(cursor)
    print('每筆資料的 resume token:: \n{}\n'.format(cursor.resume_token))
    print('傳回的內容::')
    pprint(document)
