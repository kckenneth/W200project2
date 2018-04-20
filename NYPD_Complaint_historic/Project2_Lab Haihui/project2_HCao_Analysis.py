#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 23:27:55 2018

@author: HaihuiCao
"""

import sys
print(sys.version)
import numpy as np
print(np.__version__)
import pandas as pd
print(pd.__version__)
import matplotlib.pyplot as plt
import csv
import datetime

#d = lambda x: pd.datetime.strptime(x, '%d-%b-%y')
#df = pd.read_csv('NYPD_Complaint_Data_Historic.csv',index_col=False, 
#                 parse_dates = ['CMPLNT_FR_DT','CMPLNT_TO_DT','RPT_DT'],
#                 date_parser=d)

#df = pd.read_csv('NYPD_Complaint_Data_Historic.csv',index_col=False,
#                parse_dates = ['CMPLNT_FR_DT','CMPLNT_TO_DT','RPT_DT'])

df = pd.read_csv('NYPD_Complaint_Data_Historic.csv')

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.columns)

df = df.drop(['PARKS_NM','HADEVELOPT'],axis =1)
print(df.shape)
print(df.columns)

# column CMPLNT_FR_DT

print(df.CMPLNT_FR_DT.value_counts())
print(df.CMPLNT_FR_DT.count())
print(df.CMPLNT_FR_DT.isnull().any())
df=df.dropna(subset = ['CMPLNT_FR_DT'])
print(df.shape)
print(df.CMPLNT_FR_DT.min(),df.CMPLNT_FR_DT.max())

df = df.copy()[df['CMPLNT_FR_DT'] >= '01/01/2006']
print(df.shape)
print(df.CMPLNT_FR_DT.min(), df.CMPLNT_FR_DT.max())

# to datetime
df['CMPLNT_FR_DT']=pd.to_datetime(df['CMPLNT_FR_DT'],errors = 'coerce')
print(df.CMPLNT_FR_DT.count())
print(df.CMPLNT_FR_DT.isnull().any())
df=df.dropna(subset = ['CMPLNT_FR_DT'])
print(df.shape)

df.groupby(df.CMPLNT_FR_DT.dt.to_period("Y")).OFNS_DESC.count()
df.head()

df = df[(df['CMPLNT_FR_DT'] >= '2006-1-1') & (df['CMPLNT_FR_DT'] <= '2016-12-31')]

print(df.CMPLNT_FR_DT.count())
print(df.CMPLNT_FR_DT.isnull().any())
df.groupby(df.CMPLNT_FR_DT.dt.to_period("Y")).OFNS_DESC.count()
df.groupby(df.CMPLNT_FR_DT.dt.to_period("Y")).OFNS_DESC.count().plot()
plt.ylabel("Total Crime Counts")



# combine CMPLNT_FR_DT and CMPLNT_TO_TM and to datetime
print(df.CMPLNT_TO_TM.isnull().any())

df['CMPLNT_FR']=pd.to_datetime(df['CMPLNT_FR_DT'] + ' ' + df['CMPLNT_TO_TM'],errors = 'coerce')
print(df.CMPLNT_FR.value_counts())
print(df.CMPLNT_FR.count())

df=df.dropna(subset = ['CMPLNT_FR'])
print(df.shape)
df.groupby(df.CMPLNT_FR.dt.to_period("Y")).OFNS_DESC.count().plot()

# column CMPLNT_TO_DT

df['CMPLNT_TO']=pd.to_datetime(df['CMPLNT_TO_DT'] + ' ' + df['CMPLNT_TO_TM'],errors = 'coerce')

# column RPT_DT
df.RPT_DT.isnull().any()
print(df.RPT_DT.min(),df.RPT_DT.max())

df['RPT_DT'] =  pd.to_datetime(df['RPT_DT'],errors = 'coerce')
print(df.RPT_DT.min(),df.RPT_DT.max())
df.groupby(df.RPT_DT.dt.to_period("Y")).OFNS_DESC.count()
df = df[(df['RPT_DT'] >= '2006-1-1') & (df['RPT_DT'] <= '2016-12-31')]
df.groupby(df.RPT_DT.dt.to_period("Y")).OFNS_DESC.count().plot()
plt.ylabel("Total Crime Counts")



df.head()
df.BORO_NM.value_counts()
print(df.BORO_NM.isnull().any())
print(df.BORO_NM.count())

df.BORO_NM.value_counts().plot(kind='bar')
plt.xlabel("Crime Location")
plt.ylabel("Crime Counts")

df.OFNS_DESC.value_counts().head(10)
df.OFNS_DESC.value_counts().head(10).plot(kind='bar')
plt.ylabel("Crime Counts")


#df.to_csv('NYPD_Complaint_Data_Historic_1.csv',sep='\t', encoding='utf-8',index=False)
#df = pd.read_csv('NYPD_Complaint_Data_Historic_1.csv',sep='\t')


df['RPT_DT'] =  pd.to_datetime(df['RPT_DT'])

print(df.RPT_DT.min(),df.RPT_DT.max())

year = df.groupby(df.RPT_DT.dt.to_period("Y"))
year.OFNS_DESC.count()
year.OFNS_DESC.count().plot()
plt.ylabel("Total Crime Counts")





