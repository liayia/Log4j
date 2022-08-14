import pymongo
client = pymongo.MongoClient(['localhost:20000', 'localhost:20001', 'localhost:20002'])
db = client.test

def transaction(session):
    db.test.insert_one({ 'name': 'David' }, session=session)
    ret = input("enter '1' to commit, others rollback: ")
    if ret != "1":
        raise ValueError

try:
    with client.start_session() as session:
        with session.start_transaction():
            transaction(session)
except:
    print('transaction fail')
