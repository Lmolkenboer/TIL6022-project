# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:56:40 2022

@author: pim
"""

#Percentage of male vs female shopping per category
df = px.data.tips()
fig = px.histogram(
    df, x="total_bill", y="tip", color="sex", 
    hover_data=df.columns
)
fig.show()
