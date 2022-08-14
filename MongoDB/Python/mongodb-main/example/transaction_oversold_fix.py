import pymongo

client = pymongo.MongoClient(['localhost:20000', 'localhost:20001', 'localhost:20002'])
db = client.test

def init():
    db.product.drop()
    db.product.insert_one({'_id': 1, 'value': 10})

def buy():
    try:
        with client.start_session() as session:
            with session.start_transaction():
                ## 寫入
                db.product.update_one(
                    { '_id': 1 }, 
                    { '$inc': { 'value': -1 }},
                    session=session
                )
            
                ## 讀取
                doc = db.product.find_one(
                    {'_id': 1}, 
                    session=session
                )
                
                ## 判斷
                if doc['value'] >= 0:
                    print('賣出一個')
                else:
                    raise ValueError
                
    except ValueError:
        pass
        
    except pymongo.errors.OperationFailure:
        import time
        import random
        
        time.sleep(random.random())
        doc = db.product.find_one({'_id': 1})
        if doc['value'] > 0:
            buy()
            
    except:
        pass

def report():
    doc = db.product.find_one({'_id': 1})
    print('剩餘商品數量: {value}'.format(**doc))
    
# def main():    
#     ret = input('重設商品數量？(y/n)')
#     if ret.lower() == 'y':
#         init()    
#     buy()
#     report()
    
def main():
    import threading
    import time
    
    init()
    n = threading.active_count()
    for _ in range(300):
        threading.Thread(target=buy).start()
        
    while threading.active_count() > n:
        time.sleep(0.01)
    report()
    
main()


