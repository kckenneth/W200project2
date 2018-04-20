#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 12:31:22 2018

@author: Kenneth Chen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading data
#data_all = pd.read_csv('NYPD_Complaint_Data_Historic.csv', header=None, 
#                       parse_dates=[[1, 2], 
#                                    [3, 4]])

data_all = pd.read_csv('NYPD_Complaint_Data_Historic.csv')
# Since the data contains the header, don't use header=None

"""
0            CMPLNT_NUM
1          CMPLNT_FR_DT
2          CMPLNT_FR_TM
3          CMPLNT_TO_DT
4          CMPLNT_TO_TM
5                RPT_DT
6                 KY_CD
7             OFNS_DESC
8                 PD_CD
9               PD_DESC
10     CRM_ATPT_CPTD_CD
11           LAW_CAT_CD
12           JURIS_DESC
13              BORO_NM
14          ADDR_PCT_CD
15    LOC_OF_OCCUR_DESC
16        PREM_TYP_DESC
17             PARKS_NM
18           HADEVELOPT
19           X_COORD_CD
20           Y_COORD_CD
21             Latitude
22            Longitude
23              Lat_Lon
"""

# Dropping empty or unimportant columns
data_all.drop([17, 18], axis=1, inplace=True)

data_all.columns = range(data_all.shape[1])

# Column information
data_all.loc[0]

"""
0            CMPLNT_NUM
1          CMPLNT_FR_DT
2          CMPLNT_FR_TM
3          CMPLNT_TO_DT
4          CMPLNT_TO_TM
5                RPT_DT
6                 KY_CD
7             OFNS_DESC
8                 PD_CD
9               PD_DESC
10     CRM_ATPT_CPTD_CD
11           LAW_CAT_CD
12           JURIS_DESC
13              BORO_NM
14          ADDR_PCT_CD
15    LOC_OF_OCCUR_DESC
16        PREM_TYP_DESC
17           X_COORD_CD
18           Y_COORD_CD
19             Latitude
20            Longitude
21              Lat_Lon
"""

# Dropping rows with Nan value in important columns
data_all.dropna(subset=[1, 2, 3, 4, 7, 9, 13, 19, 20], inplace=True)

# Dropping the header, the first row with description
data_all = data_all.drop([0])

# Resetting the row index
data_all = data_all.reset_index(drop=True)

# Combining date and time into a single column
data_all['FR_datetime'] = data_all[1] + ' ' + data_all[2]
data_all['TO_datetime'] = data_all[3] + ' ' + data_all[4]

# Splitting the data to faciliate data manipulation
data_all_1 = data_all[:1000000]
data_all_2 = data_all[1000001:2000000]
data_all_3 = data_all[2000001:3000000]
data_all_4 = data_all[3000001:]

def lookup(s):
    dates = {date:pd.to_datetime(date, 
                                 errors='coerce', 
                                 format="%m/%d/%y %H:%m:%s", 
                                 infer_datetime_format=True) 
    for date in s.unique()}
    return s.map(dates)

data_all_1['FR_datetime'] = lookup(data_all_1['FR_datetime'])
data_all_1['TO_datetime'] = lookup(data_all_1['TO_datetime'])

data_all_2['FR_datetime'] = lookup(data_all_2['FR_datetime'])
data_all_2['TO_datetime'] = lookup(data_all_2['TO_datetime'])

data_all_3['FR_datetime'] = lookup(data_all_3['FR_datetime'])
data_all_3['TO_datetime'] = lookup(data_all_3['TO_datetime'])

data_all_4['FR_datetime'] = lookup(data_all_4['FR_datetime'])
data_all_4['TO_datetime'] = lookup(data_all_4['TO_datetime'])

# duration
data_all_1['duration'] = data_all_1['TO_datetime'] - data_all_1['FR_datetime']
data_all_1['total_mins'] = (data_all_1['duration'].dt.days)*1440 + (data_all_1['duration'].dt.seconds/60)
    
data_all_2['duration'] = data_all_2['TO_datetime'] - data_all_2['FR_datetime']
data_all_2['total_mins'] = (data_all_2['duration'].dt.days)*1440 + (data_all_2['duration'].dt.seconds/60)
    
data_all_3['duration'] = data_all_3['TO_datetime'] - data_all_3['FR_datetime']
data_all_3['total_mins'] = (data_all_3['duration'].dt.days)*1440 + (data_all_3['duration'].dt.seconds/60)
    
data_all_4['duration'] = data_all_4['TO_datetime'] - data_all_4['FR_datetime']
data_all_4['total_mins'] = (data_all_4['duration'].dt.days)*1440 + (data_all_4['duration'].dt.seconds/60)
    
# Merging all split data
data_all_dt = pd.concat([data_all_1, data_all_2, data_all_3, data_all_4], 
                        ignore_index = True)
    
data_all_dt = data_all_dt.reset_index(drop = True)

# Saving point 1
data_all_dt.to_csv('data_all_s1.csv')

# Extracting the years
data_all_dt['fr_years'] = data_all_dt['FR_datetime'].dt.year
data_all_dt['to_years'] = data_all_dt['TO_datetime'].dt.year

data_all_dt['fr_years'].value_counts()
data_all_dt['to_years'].value_counts()

#def process_min(row):
#    if row.days_taken == 0:
#        return (data_all_1['duration'].dt.seconds)/60
#data_all_1.loc[:, 'minutes_taken'] = data_all_1.apply(process_min, axis=1)
## Taking so long, so interrupted

data_all_dt['total_mins'].value_counts().plot.pie(autopct="%1.02f%%", radius=1)

data_all_dt[13].value_counts().plot.pie(autopct="%1.02f%%", radius=1)

data_all_dt[7].value_counts()
data_all_dt[7].value_counts().plot.pie(autopct="%1.02f%%", radius=1)


data_all_dt[9].value_counts()
data_all_dt[9].value_counts().plot.pie(autopct="%1.02f%%", radius=1)

data_all_crimes_city = data_all_dt.groupby([13, 7])



# Taking out all years less than 2005 crime
data_all_dt.loc[data_all_dt['to_years'] == 2017, [1, 3, 7, 13]]

data_all_dt_range = data_all_dt[data_all_dt.to_years > 2005]

data_all_dt_range = data_all_dt[data_all_dt.fr_years > 2005]

data_all_dt_range['fr_years'] = data_all_dt_range['FR_datetime'].dt.year
data_all_dt_range['to_years'] = data_all_dt_range['TO_datetime'].dt.year

data_all_dt_range['fr_years'].value_counts().sort_index(ascending=False).plot.pie(autopct="%1.02f%%", radius=1)

data_all_dt_range['to_years'].value_counts().sort_index(ascending=False)

# Grouping by year and criminal activity
x = data_all_dt_range.groupby([7, 'fr_years'])
x.size()

x.size().unstack()

x.size().unstack().to_csv('year_crime.csv')

y = data_all_dt_range.loc[data_all_dt_range[7] == 'HARRASSMENT 2', 13]

z = data_all_dt_range.groupby([data_all_dt_range.loc[data_all_dt_range[7] == 'HARRASSMENT 2', 13], 'fr_years'])

z.size().unstack().plot.bar()

data_all_dt_range[7].value_counts().plot.pie(autopct="%1.02f%%", radius = 1)

data_all_dt_range[13].value_counts().plot.pie(autopct="%1.02f%%", radius = 1)

x = data_all_dt_range.groupby([7, 'years'])


# Making a new feature 'days_taken'
data_all_dt_range['days_taken'] = data_all_dt_range['duration'].dt.days

data_all_dt_range.to_csv('data_all_dt_range.csv')

# Splitting the data to faciliate data manipulation
data_all_dt_range_1 = data_all_dt_range[:1000000]
data_all_dt_range_2 = data_all_dt_range[1000001:2000000]
data_all_dt_range_3 = data_all_dt_range[2000001:3000000]
data_all_dt_range_4 = data_all_dt_range[3000001:]

data_all_dt_range_1.to_csv('data_all_dt_range_1.csv')