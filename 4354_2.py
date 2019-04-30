# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:15:22 2019

@author: PC
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:\Users\PC\Desktop\CS 4354')

df = pd.read_csv('DDS.csv')

df2 = df.groupby(["incidentType"], as_index=False)['placeCode'].count()

itype = pd.Series(df2["incidentType"].values)
count = pd.Series(df2["placeCode"].values)

df3 = pd.concat([itype, count], axis = 1)

df4 = df3.sort_values(by=[1], ascending =True)

sort_state = pd.Series(df4[0].values)
sort_count = pd.Series(df4[1].values)
state_arr = []
count_arr = []
for i in sort_state:
    state_arr.append(i)
for j in sort_count:
    count_arr.append(j)

plt.rcParams['figure.figsize'] = (19, 13.0)
plt.barh(sort_state, sort_count,  color=['r','b','m','gray'], alpha=0.8)
plt.yticks(itype)
plt.xlim(0,4200)
plt.xlabel("Count")
for i, v in enumerate(count_arr):
    plt.text(v + 15, i, str(v), color='black', fontweight='bold')
plt.title("Disaster Count in Each State")
plt.show()















