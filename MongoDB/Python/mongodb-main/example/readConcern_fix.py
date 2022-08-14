import pymongo
from pymongo.write_concern import WriteConcern
from pymongo.read_concern import ReadConcern
import time

hosts = ['localhost:20000', 'localhost:20001', 'localhost:20002']
client = pymongo.MongoClient(hosts, readPreference='secondary')
db = client.test

with client.start_session(causal_consistency=True) as session:
    for n in range(100):
        # Primary 寫資料
        db.test.drop()
        result = db.test.with_options(
            # 多台接收到資料
            write_concern=WriteConcern(w='majority', j=True)
            # 只要有一台接收到資料
            #write_concern=WriteConcern(w=1, j=True)
        ).insert_one({'name': 'aaa', 'n': n}, session=session)

        id = None
        if result.acknowledged:
            id = result.inserted_id
        else:
            print('error')

        # Secondary 讀資料
        doc = db.test.with_options(
            #read_concern=ReadConcern(level='local')
            read_concern=ReadConcern(level='majority')
        ).find_one(({'_id': id}), session=session)
    
        print(doc)
        time.sleep(1)
