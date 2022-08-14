import pymongo
from pymongo.write_concern import WriteConcern
from pymongo.read_concern import ReadConcern

hosts = ['localhost:20000', 'localhost:20001', 'localhost:20002']
client = pymongo.MongoClient(hosts, readPreference='secondary')
db = client.test

# Primary 寫資料
db.test.drop()
db.test.with_options(
    write_concern=WriteConcern(w='majority', j=True)
).insert_one({'name': 'aaa'})

# Secondary 讀資料
doc = db.test.with_options(
    read_concern=ReadConcern(level='local')
).find_one()
print(doc)
