#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
from matplotlib import pyplot as plt
os.chdir(r'C:\Users\zxc63\Downloads')
df=pd.read_csv('DisasterDeclarationsSummaries.csv')
df=df.sort_values(by='disasterNumber' )
df1=df.groupby(['disasterType'])[['state']]
## Select
df_sub1=df[ df['fyDeclared'] > 2018 ]
## Insert
df_sub2=df_sub1.append({'disasterNumber':1	,'ihProgramDeclared':0	,'iaProgramDeclared':1	,'paProgramDeclared':1	,'hmProgramDeclared':1	 ,'state':	'GA'	,'declarationDate':'1953-05-02T00:00:00.000Z'	,'fyDeclared':	1953	,'disasterType':	'DR'	,'incidentType':'Tornado'		,'title':'TORNADO'		,'incidentBeginDate':'1953-05-02T00:00:00.000Z'		,'incidentEndDate':'1953-05-02T00:00:00.000Z'		,'disasterCloseOutDate':'1954-06-01T00:00:00.000Z'		,'hash'	:'e6f77c3a97c63d478bf14c9a58f60a0d'	,'lastRefresh':	'2018-02-09T14:38:26.149Z'
} , ignore_index=True)
## Update
df_sub3=df_sub1
df_sub3.iloc[0,5]='TX'
## Delete
df_sub4=df_sub1
df_sub4=df_sub4.drop(49131)
## Select distinct disaster 
df_distinct=df.drop_duplicates(['incidentType'])
## Select disaster Type 
df_Tornado=df[df['incidentType']=='Tornado']
df_Fire=df[df['incidentType']=='Fire']
df_Flood=df[df['incidentType']=='Flood']
df_Hurricane=df[df['incidentType']=='Hurricane']
df_Volcano=df[df['incidentType']=='Volcano']
df_Earthquake=df[df['incidentType']=='Earthquake']
df_SevereStorm=df[df['incidentType']=='Severe Storm(s)']
df_Drought=df[df['incidentType']=='Drought']
df_Typhoon=df[df['incidentType']=='Typhoon']
df_ToxicSubstance=df[df['incidentType']=='Toxic Substances']
df_CoastalStorm=df[df['incidentType']=='Coastal Storm']
df_Chemical=df[df['incidentType']=='Chemical']
df_Dam_LeveeBreak=df[df['incidentType']=='Dam/Levee Break']
df_FishingLosses=df[df['incidentType']=='Fishing Losses']
df_Frezzing=df[df['incidentType']=='Freezing']
df_SevereIcStorm=df[df['incidentType']=='Severe Ice Storm']
df_Terrorist=df[df['incidentType']=='Terrorist']
df_Other=df[df['incidentType']=='Other']

data=[465,1292,3040,9957,301,10555,297,1990,16201,1435]

plt.pie(data,labels=['Coastal Storm','Drought','Fire','Flood','Freezing','Hurricane','other','Severe Ice Storm ','Severe Strom','Tornado',],autopct='%1.0f%%', shadow=True, pctdistance=1.1, labeldistance=1.2)

plt.tight_layout()

ax1.axis('equal')
plt.show()

