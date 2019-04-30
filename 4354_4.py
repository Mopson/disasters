# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:20:19 2019

@author: PC
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

os.chdir('C:\Users\PC\Desktop\CS 4354')

df = pd.read_csv('DDS.csv')
df5060s = df.loc[(df['fyDeclared'] >1950) & (df['fyDeclared'] <1970)]
df7080s = df.loc[(df['fyDeclared'] >1970) & (df['fyDeclared'] <1990)]
df9000s = df.loc[(df['fyDeclared'] >1990) & (df['fyDeclared'] <2010)]

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list = ["1950s & 1960s", "1970s & 1980s", "1990s &2000s"]  
size = [1706, 7459, 26998]   
color = ["red", "blue", "green"]   
explode = [0, 0, 0] 

patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
plt.axis("equal")
plt.title("Plate Graph of Disasters in Different Times")
plt.legend()
plt.show()