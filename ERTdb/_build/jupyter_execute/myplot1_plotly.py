#!/usr/bin/env python
# coding: utf-8

# # My plot 1 with plotly

# In[1]:


import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()


# A bit more text here

# <div class="alert alert-info">
# 
# And a note here
# 
# </div>

# In[ ]:




