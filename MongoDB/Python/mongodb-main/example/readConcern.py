import pymongo
from pymongo.write_concern import WriteConcern
from pymongo.read_concern import ReadConcern
import time

hosts = ['localhost:20000', 'localhost:20001', 'localhost:20002']
client = pymongo.MongoClient(hosts, readPreference='secondary')
db = client.test

db.test.drop()
#with client.start_session() as session:
for n in range(100):
    # Primary 寫資料
    result = db.test.with_options(
        write_concern=WriteConcern(w='majority', j=True)
    ).insert_one({'name': 'aaa', 'n': n})

    id = None
    if result.acknowledged:
        id = result.inserted_id
    else:
        print('error')

    # Secondary 讀資料
    doc = db.test.with_options(
        read_concern=ReadConcern(level='majority')
    ).find({'_id': id})
    print(list(doc))
    time.sleep(1)
