#!/usr/bin/env python
# coding: utf-8

# # ANLY503 A5 Altair

# ## Load Pacakage

# In[1]:


import altair as alt
import pandas as pd
import numpy as np


# ## Read Data

# In[2]:


data=pd.read_csv('eco/cleaned_data1.csv')


# Convert data type.

# In[3]:


data['Consumption']=data['Consumption'].round(2)
data['Date']=pd.to_datetime(data['Date'])


# Draw an interactive multiple plot.

# In[4]:


selection=alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['Date'], empty='none')



scale = alt.Scale(domain=['Entertainment', 'Freezer', 'Fridge', 
                          'Kitchen appliance','Lamp','Microwave',
                          'Sterep and laptop','Tablet'],
                  range=['#13eac9', '#ae7181', '#cdfd02', 
                         '#3d1c02', '#9467bd','#bccb7a'
                         ,'#d5869d','#ff5b00'])

colors = alt.Color('Part:N', scale=scale) 


base=alt.Chart(data,title='Diiferent Part Electric Consumption ').mark_line(
    interpolate='basis').encode(x=alt.X('Date:T', title='Date'),
    y=alt.X('Consumption:Q', title='Consumption(Millions)'),
    color=colors)


click=alt.Chart(data).mark_point().encode(
    x='Date:T',opacity=alt.value(0),).add_selection(selection)


points=base.mark_point().encode(
    opacity=alt.condition(selection, alt.value(1), alt.value(0)))


text = base.mark_text(align='left', dx=10, dy=5).encode(
    text=alt.condition(selection, 'Consumption:Q', alt.value(' ')))

rules = alt.Chart(data).mark_rule(color='gray').encode(
    x='Date:T',).transform_filter(selection)

fig=alt.layer(base, click, points, rules, text).properties(
    width=900, height=500).configure_title(fontSize=24).interactive()
fig


# In[5]:


fig.save('docs/altair.html')

