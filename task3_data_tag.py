# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:43:22 2021

@author: Administrator
"""

import pandas as pd
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os


# def str2int(dt):
#     errordata=dt['W_Error']
#     errordata[errordata!='E016']=0
#     errordata[errordata=='E016']=1
#     errordata.replace(1,1,inplace=True)
#     errordata.replace(0,0,inplace=True)
#     gunnum=dt['gun_no']
#     gunval=pd.get_dummies(gunnum).columns
#     for i in range(len(gunval)):
#         gunnum.replace(gunval[i],i,inplace=True)
#     return dt


errordex0 = 0
path = 'train/'
pathlist = os.listdir(path)
data = pd.read_pickle(path+'05-18.pkl')
data['day'] = 18
# for i in pathlist[16:24]:
#     data1=pd.read_pickle(path+i)
#     filename=int(i[3:5])
#     data1['day']=filename
#     data=pd.concat([data,data1],axis=0)
    
# data=pd.read_pickle('7_14-18.pkl')
data = data.sort_values(by=['gun_no', 'time'])
data.index = [i for i in range(len(data.index))]
errordata = data['W_Error']
timeline = data['time']
gunnum = data['gun_no']
lifetime = data['C_Cylinder_force']


locallist=[]
for j in range(1, 13):
    inlocal = list(gunnum).index(j)
    locallist.append(inlocal)
locallist.append(len(gunnum))

p = 0
tp1 = 0
for j in range(13):
    q = locallist[j]
    for temp in range(p, q):
        if temp % 2000 == 0:
            print(temp/70000)
        if errordata[temp] == 1:
            for i in range(temp, tp1-1, -1):
                lifetime[i]= int(timeline[temp]-timeline[i])
            tp1 = temp
    p = q
    temptime = timeline[q-1]
    if tp1 != q:
        for i in range(tp1, q):
            lifetime[i] = 432000
        tp1 = q
    tp1 = q
    print(j)

data['C_Cylinder_force']=lifetime
# data.to_csv('task3_0718.csv')
data.to_pickle('task3_0710-18.pkl')


# dayindex=[]
# data=data.sort_values(by=['day'])
# for i in range(10,19):
#     p=list(data['day']).index(i)
#     dayindex.append(p)
# dayindex.append(len(data.index))
# for i in range(9):
#     p=dayindex[i]
#     q=dayindex[i+1]
#     datak=data.iloc[p:q,:]
#     datak=datak.drop(['day'],axis=1)
#     datak.to_pickle('datak/07-1'+str(i)+'.pkl')


