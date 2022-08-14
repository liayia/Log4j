from tkinter import E
import pymongo

client = pymongo.MongoClient(['localhost:20000', 'localhost:20001', 'localhost:20002'])
db = client.test

def init():
    db.product.drop()
    db.product.insert_one({'_id': 1, 'value': 10})

def buy():
    ## 讀取
    doc = db.product.find_one({'_id': 1})
    ## 判斷
    if doc['value'] > 0:
        ## 寫入
        db.product.update_one(
            { '_id': 1 }, 
            { '$inc': { 'value': -1 }}
        )
    else:
        print('賣完了')

def report():
    doc = db.product.find_one({'_id': 1})
    print('剩餘商品數量: {value}'.format(**doc))
    
def main():    
    ret = input('重設商品數量？(y/n)')
    if ret.lower() == 'y':
        init()    
    buy()
    report()
    
# def main():
#     import threading
#     import time
#     
#     init()
#     n = threading.active_count()
#     for _ in range(300):
#         threading.Thread(target=buy).start()
#         
#     while threading.active_count() != n:
#         time.sleep(0.01)
#     report()
    
main()


