#!/usr/bin/env python
# coding: utf-8

# # ANLY503 A5 Data Munging

# ## Load Pacakage

# In[1]:


import pandas as pd
import glob
import re
from datetime import datetime


# ## Read Data

# Set functions to read multiple csv file into dataframeSet 

# In[2]:


def file_read(path,names):
    files = glob.glob(path + names)
    dfs = [pd.read_csv(f, header=None, sep=";") for f in files]
    consumption=[]
    for i in dfs:
        consumption.append(sum(i[0])/1000000)
    date=[]
    for i in files:
        time = re.search(r'\d{4}-\d{2}-\d{2}', i)
        d=datetime.strptime(time.group(), '%Y-%m-%d').date()
        date.append(d)
    #data=pd.DataFrame()
    #data['Date']=date
    #data['Consumption']=Consumption
    #data['Part']=part
    return consumption,date

def folder_read(path):
    a1,b1=file_read(path,"/2012-07*.csv")
    a2,b2=file_read(path,"/2012-08*.csv")
    a3,b3=file_read(path,"/2012-09*.csv")
    a4,b4=file_read(path,"/2012-10*.csv")
    a5,b5=file_read(path,"/2012-11*.csv")
    a6,b6=file_read(path,"/2012-12*.csv")
    a=a1+a2+a3+a4+a5+a6
    b=b1+b2+b3+b4+b5+b6
    return a,b

def df_creat(part,path):
    df=pd.DataFrame()
    df['Consumption'],df['Date']=folder_read(path)
    df['Part']=part
    return(df)


# Read all folders on 04 foloder

# In[3]:


df1=df_creat('Fridge','eco/04/01')
df2=df_creat('Kitchen appliances','eco/04/02')
df3=df_creat('Lamp','eco/04/03')
df4=df_creat('Stereo and laptop','eco/04/04')
df5=df_creat('Freezer','eco/04/05')
df6=df_creat('Tablet','eco/04/06')
df7=df_creat('Entertainment','eco/04/07')
df8=df_creat('Microwave','eco/04/08')


# ## Create Data

# Create first analysis Data

# In[4]:


data1=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])
data1.sample(10)


# Create second analysis Data

# In[5]:


data2=data1
data2['Month']=pd.DatetimeIndex(data2['Date']).month_name(locale='English')
data2_1=data1.groupby(['Part','Month'], as_index=False).mean() 
data2_2=data1.groupby(['Part'], as_index=False).mean() 
data2_2['Month']='All'
data2=pd.concat([data2_1,data2_2])
data2.sample(10)


# Save data to local csv file.

# In[6]:


data1.to_csv('eco/cleaned_data1.csv', index=False)
data2.to_csv('eco/cleaned_data2.csv', index=False) 

