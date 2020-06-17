#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import fbprophet


# In[2]:


from fbprophet import Prophet


# In[3]:


dir(Prophet)


# In[4]:


model = Prophet()


# In[5]:


df = pd.read_csv("EURUSD1440.csv")


# In[6]:


df.columns=["date","time","open","high","low","close","volume"]


# In[7]:


df.shape


# In[8]:


df2 = df.tail(50)


# In[18]:


pd_df2 = pd.DataFrame(data=df2, columns=['date','open'])


# In[19]:


df2.plot()


# In[20]:


pd_df2['open'] = pd_df2['open'] - pd_df2['open'].shift(1)


# In[21]:


pd_df2.plot()


# In[23]:


pd_df2.tail()


# In[24]:


pd_df2.rename(columns={"date":"ds","open":"y"}, inplace=True)


# In[25]:


pd_df2.head()


# In[28]:


pd_df2 = pd_df2[2:]


# In[29]:


pd_df2.head()


# In[30]:


model.fit(pd_df2)


# In[31]:


future_dates = model.make_future_dataframe(periods=15)


# In[32]:


future_dates.shape


# In[47]:


future_dates.tail()


# In[34]:


prediction = model.predict(future_dates)


# In[35]:


prediction.head()


# In[36]:


model.plot(prediction)


# In[37]:


model.plot_components(prediction)


# In[39]:


pd_df2.shape


# In[42]:


#start validation
from fbprophet.diagnostics import cross_validation


# In[ ]:




