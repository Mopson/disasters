# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:47:32 2019

@author: PC
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir('C:\Users\PC\Desktop\CS 4354')

df = pd.read_csv('Declare_date_year.csv')

dfTX=df.loc[df['state'] =="TX"]
dfGA=df.loc[df['state'] =="GA"]
dfNY=df.loc[df['state'] =="NY"]
dfOK=df.loc[df['state'] =="OK"]
dfCT=df.loc[df['state'] =="CT"]
dfMA=df.loc[df['state'] =="MA"]
dfLA=df.loc[df['state'] =="LA"]

disTX = dfTX["fyDeclared"].unique()
disGA = dfGA["fyDeclared"].unique() 
disNY = dfNY["fyDeclared"].unique()
disOK = dfOK["fyDeclared"].unique()
disCT = dfCT["fyDeclared"].unique()
disMA = dfMA["fyDeclared"].unique()
disLA = dfLA["fyDeclared"].unique()

arr1 =[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
arr6=[]
arr7=[]

for i in range(0,58):
    arr1.append(5)
    i+=1
for i in range(0,36):
    arr2.append(7)
    i+=1
for i in range(0,45):
    arr3.append(9)
    i+=1
for i in range(0,45):
    arr4.append(11)
    i+=1
for i in range(0,24):
    arr5.append(13)
    i+=1
for i in range(0,28):
    arr6.append(15)
    i+=1
for i in range(0,45):
    arr7.append(17)
    i+=1

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
color = ['gray','c','orange','pink','lightblue']
ax.scatter(disTX,arr1,c=color, s = 50,marker='o', alpha = 0.7)
ax.scatter(disGA,arr2,c=color, s = 50,marker='+', alpha = 0.7)
ax.scatter(disNY,arr3,c=color, s = 50,marker='*', alpha = 0.7)
ax.scatter(disOK,arr4,c=color, s = 50,marker='x', alpha = 0.7)
ax.scatter(disCT,arr5,c=color, s = 50,marker='s', alpha = 0.7)
ax.scatter(disMA,arr6,c=color, s = 50,marker='p', alpha = 0.7)
ax.scatter(disLA,arr7,c=color, s = 50,marker='d', alpha = 0.7)
ax.set_yticks([0,5,7,9,11,13,15,17])
ax.set_yticklabels([0,'TX','GA','NY','OK','CT','MA','LA'])
plt.xlabel("Year")
plt.ylabel("State")
plt.title("Disaster Distribution of States in Each Year")
plt.show()



