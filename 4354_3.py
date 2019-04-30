# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:07:44 2019

@author: PC
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:15:22 2019

@author: PC
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:\Users\PC\Desktop\CS 4354')

df = pd.read_csv('Declare_date_year.csv')

df2 = df.groupby(["fyDeclared"], as_index=False)['declarationDate'].count()

year = pd.Series(df2["fyDeclared"].values)
count = pd.Series(df2["declarationDate"].values)

count_arr = []
for i in count:
    count_arr.append(i)

plt.rcParams['figure.figsize'] = (19, 13)
plt.bar(year, count, color=['red','orange','blue','gray'], alpha=0.8)
plt.xticks(year)
plt.xlim(0,5000)
plt.xlabel("Year")
for i, v in enumerate(count_arr):
    plt.text(i, v, v, color='black', fontweight='bold')
plt.title("Disaster Count in Each Year")
plt.show()















