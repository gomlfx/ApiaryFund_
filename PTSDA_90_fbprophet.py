#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('EURUSD1440.csv')


# In[3]:


df.columns=["date","time","open","high","low","close","volume"]
df['datetime'] = df['date'] + " " + df['time']
pd_df1_5 = pd.DataFrame(data=df, columns=['datetime','close'])
pd_df2 = pd.DataFrame(data = pd_df1_5.tail(240))
pd_df2.rename(columns={"datetime":"ds","close":"y"}, inplace=True)
df = pd_df2
df['ds'] = pd.to_datetime(df['ds'])
df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


m = Prophet(daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=True) #daily_seasonality=True, weekly_seasonality=True,yearly_seasonality=True
m.fit(df)


# In[7]:


future = m.make_future_dataframe(periods=5,freq='D')


# In[8]:


future.tail()


# In[9]:


len(df)


# In[10]:


len(future)


# In[11]:


forecast = m.predict(future) 


# In[12]:


forecast.head()


# In[13]:


forecast[['ds','yhat_lower','yhat_upper','yhat']].tail()


# In[14]:


m.plot(forecast)
plt.xlim('2020-07-13','2020-07-20')
plt.ylim(1.12,1.16) 


# In[15]:


m.plot_components(forecast);


# In[16]:


from fbprophet.plot import add_changepoints_to_plot
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast) 


# In[17]:


df.info()


# In[18]:


len(df)


# In[41]:


#train/test split
train = df.iloc[:235]
test = df.iloc[235:]


# In[42]:


#fit prophet on train set
m = Prophet(daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=True)#daily_seasonality=True, weekly_seasonality=True, yearly_seasonality=True) #later use seasonality: daily_seasonality=True,weekly_seasonality=True,yearly_seasonality=True
m.fit(train)
#predict out length of test set
future = m.make_future_dataframe(periods=5, freq='D')
forecast = m.predict(future)


# In[43]:


forecast.tail()


# In[44]:


test


# In[45]:


ax = forecast.plot(x='ds',y='yhat',label='Predictions',legend=True, figsize=(12,8))
test.plot(x='ds',y='y',label='True Test Data',legend=True,ax=ax,xlim=('2020-07-01','2020-07-30'),ylim=(1.12,1.16))


# In[46]:


from statsmodels.tools.eval_measures import rmse


# In[47]:


predictions = forecast.iloc[-5:]['yhat']


# In[48]:


predictions


# In[49]:


test['y']


# In[50]:


rmse(predictions,test['y'])


# In[51]:


test.mean()


# In[52]:


from fbprophet.diagnostics import cross_validation,performance_metrics
from fbprophet.plot import plot_cross_validation_metric


# In[53]:


initial = 5 * 48
initial = str(initial)+' days'


# In[54]:


initial


# In[55]:


period = 5 * 48
period=str(period)+' days'


# In[56]:


horizon = 48
horizon = str(horizon) + ' days'


# In[57]:


df_cv=cross_validation(m,initial=initial,period=period,horizon=horizon)


# In[58]:


df_cv.head()


# In[59]:


df_cv.tail()


# In[60]:


len(df_cv)


# In[61]:


performance_metrics(df_cv)


# In[62]:


plot_cross_validation_metric(df_cv,metric='mape');


# In[ ]:




