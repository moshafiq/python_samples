#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install yfinance


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


# In[3]:


stock_symbol = 'AAPL'  
start_date = '2020-01-01'
end_date = '2021-12-31'


# In[4]:


stock_data = yf.download(stock_symbol, start=start_date, end=end_date)


# In[5]:


stock_data


# In[6]:


print(stock_data.head())


# In[7]:


print(stock_data.describe())


# In[8]:


plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
plt.title(f'{stock_symbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()


# In[9]:


plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Volume'], label='Volume', color='green')
plt.title(f'{stock_symbol} Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




