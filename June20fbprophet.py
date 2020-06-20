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


#dir(Prophet)


# In[4]:


model = Prophet()


# In[5]:


df = pd.read_csv("EURUSD60.csv")


# In[6]:


df.columns=["date","time","open","high","low","close","volume"]


# In[7]:


df.tail()


# In[8]:


df.shape


# In[9]:


df.dtypes


# In[10]:


pd_df1 = pd.DataFrame(data=df, columns=['date','time'])


# In[11]:


df['datetime']=pd_df1.values.tolist()


# In[12]:


df['datetime'].tail()
#df[['datetime']] = df[['datetime']].apply(pd.to_datetime)


# In[13]:


df['datetime'] = df['date'] + " " + df['time']


# In[14]:


df['datetime']


# In[15]:


pd_df1_5 = pd.DataFrame(data=df, columns=['datetime','open'])


# In[16]:


pd_df2 = pd_df1_5.tail(200)


# In[17]:


pd_df2.tail()


# In[18]:


pd_df2.dtypes


# In[19]:


pd_df2.tail()


# In[20]:


pd_df2.plot()


# In[21]:


#pd_df2['open'] = pd_df2['open'] - pd_df2['open'].shift(1)


# In[22]:


pd_df2.plot()


# In[23]:


pd_df2.tail()


# In[24]:


pd_df2.rename(columns={"datetime":"ds","open":"y"}, inplace=True)


# In[25]:


pd_df2.head()


# In[26]:


pd_df2 = pd_df2[2:]


# In[27]:


pd_df2.head()


# In[28]:


model.fit(pd_df2)


# In[29]:


future_dates = model.make_future_dataframe(periods=24, freq='H')


# In[30]:


future_dates.shape


# In[31]:


future_dates.tail()


# In[32]:


prediction = model.predict(future_dates)


# In[33]:


prediction.tail()


# In[34]:


model.plot(prediction)


# In[35]:


model.plot_components(prediction)


# In[36]:


pd_df2.shape


# In[37]:


#start validation
from fbprophet.diagnostics import cross_validation


# In[ ]:





# In[ ]:




