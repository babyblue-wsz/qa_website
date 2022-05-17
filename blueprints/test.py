import time
from datetime import datetime
import os
from threading import Thread,Lock
from time import sleep

# 时间、日期
# before = time.time()
# sum=0
# for i in range(100000):
#    print(i)
#
# after = time.time()
# print("time is :" + str(after-before))

# 时间、日期
# timeNow = str(datetime.now())
# timeNow2 = datetime.now().strftime('%Y-%m-%d ** %H:%M:%S')
# print(timeNow)
# print(timeNow2)

# 命令
# cmd = r'e:\TOOLS\wget http://mirrors.sohu.com/nginx/nginx-1.13.9.zip'
# os.system(cmd)
# print("downloaded")

# 多线程
# def threadFunc(arg1, arg2):
#     print("子线程，开始")
#     print(f'线程函数的参数是：{arg1},{arg2}')
#     before = time.time()
#     sleep(5)
#     after = time.time()
#     print("子线程，结束，运行时间是："+str(after-before))
#
# thread = Thread(
#     target=threadFunc,
#     args=('参数1','参数2')
# )
#
# thread.start()
# thread.join()
# print("主线程结束")

# 并发操作共享数据
# bank = {
#     'byhy': 0
# }
# banklock = Lock()
#
#
# def deposit(threadID, amount):
#     # 操作共享数据前，申请获取锁
#     banklock.acquire()
#     balance = bank['byhy']
#     sleep(0.1)
#     bank['byhy'] = balance + amount
#     print(f'子线程{threadID}也结束')
#
#     # 操作完共享数据后，申请释放锁
#     banklock.release()
#
#
# threadlist = []
# for index in range(10):
#     thread = Thread(
#         target=deposit,
#         args=(index, 1)
#     )
#     thread.start()
#     threadlist.append(thread)
#
# for thread in threadlist:
#     thread.join()
#
# print("主线程结束")
# print(f'最后余额为{bank["byhy"]}')


# daemon线程
# from threading import Thread
# from time import sleep
#
# def threadFunc():
#     sleep(2)
#     print('子线程 结束')
#
# thread = Thread(target=threadFunc,
#                 daemon=True)
# thread.start()
# print('主线程结束')

# from multiprocessing import Process
# def f():
#     while True:
#         b = 53*53
#
# if __name__ == '__main__':
#     plist = []
#     # 启动10个线程
#     for i in range(2):
#         p = Process(target=f)
#         p.start()
#         plist.append(p)
#
#     for p in plist:
#         p.join()

# import json
# historyTransactions = [
#
#     {
#         'time'   : '20170101070311',  # 交易时间
#         'amount' : '3088',            # 交易金额
#         'productid' : '45454455555',  # 货号
#         'productname' : 'iphone7'     # 货名
#     },
#     {
#         'time'   : '20170101050311',  # 交易时间
#         'amount' : '18',              # 交易金额
#         'productid' : '453455772955', # 货号
#         'productname' : '奥妙洗衣液'   # 货名
#     }
#
# ]
#
# # dumps 方法将数据对象序列化为 json格式的字符串
# jsonstr = json.dumps(historyTransactions,indent=4,ensure_ascii=False)
# print(jsonstr)

# 深拷贝、浅拷贝
# import copy
#
# a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
#
# b = a  # 赋值，传对象的引用
# c = copy.copy(a)  # 对象拷贝，浅拷贝
# d = copy.deepcopy(a)  # 对象拷贝，深拷贝
#
# a.append(5)  # 修改对象a
# a[4].append('c')  # 修改对象a中的['a', 'b']数组对象
#
# print('a = ', a)
# print('b = ', b)
# print('c = ', c)
# print('d = ', d)

import xlrd
book = xlrd.open_workbook("C:\\Users\\babyblue\\Desktop\\daoluyiban.xlsx")
print(f'包含表单数量：{book.nsheets}')
print(f'表单的名称分别为：{book.sheet_names()}')
sheet = book.sheet_by_index(0)
print(f"表单名：{sheet.name} ")
print(f"表单索引：{sheet.number}")
print(f"表单行数：{sheet.nrows}")
print(f"表单列数：{sheet.ncols}")
print(f"单元格A1内容是: {sheet.cell_value(rowx=0, colx=0)}")