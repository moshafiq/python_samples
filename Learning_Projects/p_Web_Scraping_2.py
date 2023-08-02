#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[ ]:





# In[3]:


url = "https://www.scrapethissite.com/pages/forms/?per_page=100"


# In[4]:


page = requests.get(url)


# In[5]:


soup = BeautifulSoup(page.text, "html")


# In[6]:


print(soup)


# In[ ]:





# In[7]:


table = soup.find("table")
table


# In[ ]:





# In[8]:


team_data = table.find_all("th")
team_data


# In[ ]:





# In[9]:


team_data = [title.text.strip() for title in team_data]
team_data


# In[ ]:





# In[10]:


import pandas as pd


# In[11]:


df = pd.DataFrame(columns = team_data)
df


# In[ ]:





# In[12]:


column_data = table.find_all("tr")
column_data


# In[ ]:





# In[13]:


for row in column_data[1:]:
    
    row_data = row.find_all("td")
    ind_row_data = [data.text.strip() for data in row_data]
    print(ind_row_data)
    
    length = len(df)
    df.loc[length] = ind_row_data


# In[ ]:





# In[14]:


df


# In[15]:


df.to_csv(r"C:\Users\Shafiq\~ProjectData\Outputs\HockeyTeams.csv" , index = False)


# In[ ]:




