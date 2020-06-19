#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fbprophet import Prophet


# In[2]:


m = Prophet()


# In[3]:


m.add_seasonality(name="monthly", period=30, fourier_order = 5)


# In[4]:


import pandas as pd


# In[5]:


original_data = pd.read_csv("EURUSD1440.csv")


# In[6]:


original_data.columns=["date","time","open","high","low","close","volume"]


# In[7]:


original_data.tail()


# In[8]:


open = original_data[["date","open"]]


# In[9]:


open.shape


# In[10]:


open.rename(columns={"date":"ds","open":"y"}, inplace=True)


# In[11]:


train = open[12000:]


# In[12]:


test = open[1900:]


# In[13]:


train.head()


# In[14]:


#fit model
m.fit(train)


# In[15]:


future_dates = m.make_future_dataframe(periods=15)


# In[16]:


future_dates


# In[17]:


#predict
prediction = m.predict(future_dates)


# In[18]:


#plot
m.plot(prediction)


# In[19]:


m.plot_components(prediction)


# In[20]:


test


# In[21]:


test['dates'] = pd.to_datetime(test['ds'])


# In[22]:


test


# In[23]:


test = test.set_index("dates")


# In[24]:


test = test['y']


# In[25]:


import matplotlib.pyplot as plt


# In[26]:


test.plot()


# In[27]:


from fbprophet.plot import add_changepoints_to_plot


# In[28]:


fig = m.plot(prediction)
c = add_changepoints_to_plot(fig.gca(),m,prediction)


# In[ ]:




