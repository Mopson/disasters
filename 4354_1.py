# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:15:22 2019

@author: PC
"""

import pandas as pd
import os

os.chdir('C:\Users\PC\Desktop\CS 4354')

df = pd.read_csv('disaster_place.csv')

date = df.iloc[:,2]
year = df.iloc[:,3]

df2 = pd.concat([date, year], axis = 1)

df2.to_csv('Declare_area_code.csv')