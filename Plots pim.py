# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:56:40 2022

@author: pim
"""
import plotly.express as px
import plotly.graph_objects as go

#Percentage of male vs female shopping per category
df = px.data.stores_country_data()
fig = px.histogram(
    df, x="total_bill", y="tip", color="sex", 
    hover_data=df.columns
)
fig.show()

