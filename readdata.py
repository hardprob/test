import pandas as pd
import numpy as np
import time
from sqlalchemy import create_engine


#用sql读出表数据
# engine = create_engine('mysql+pymysql://root:123456@localhost/tzqc?charset=utf8mb4')
# sql = pd.read_sql('zhanghao1', engine)
# # print(sql)
# a = time.strftime("%Y-%m-%d ", time.localtime())
# datefile1 = 'D:/PIC/' + a + '.xls'
# print(type(sql.iloc[0,0]))
# for i in range(len(sql)-1):
#     b=sql.iloc[i,0]
#     data = pd.read_excel(datefile1, sheet_name=b)  # 读取数据
#     print(data)





#用excle读出数据
a = time.strftime("%Y-%m-%d ", time.localtime())
datefile1 = 'D:/PIC/' + a + '.xls'
datafile2='D:\PIC\zhanghao.xls'
data=pd.read_excel(datafile2,dtype=str)
# print(data)
# print(data.iloc[0,1])
# print(len(data))
for i in range(4):
    for j in range(20):
        a=data.iloc[i,j]
        print(a)
        b = pd.read_excel(datefile1, sheet_name=a)  # 读取数据
        print(b)
# data=data.loc[0]
# data=list(data)
# print(data[3])
# for i in range(len(data)):
#     if data[i]=='0':
#         pass
#     else:
# # # data=list[data.loc[0],data.loc[1],data.loc[2],data.loc[3]]
# data = pd.read_excel(datefile1, sheet_name='0001100911056') #读取数据
# print(data)