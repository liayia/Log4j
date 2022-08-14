import pymongo
client = pymongo.MongoClient(['localhost:20000', 'localhost:20001', 'localhost:20002'])
db = client.test

# 建立交易需要的 session
session = client.start_session()
# 交易開始
session.start_transaction()
db.test.insert_one({ 'name': 'David' }, session=session)

ret = input("enter '1' to commit, others rollback: ")
if ret == "1":
    session.commit_transaction()
else:
    session.abort_transaction()
