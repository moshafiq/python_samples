#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")


# In[ ]:





# In[3]:


print(soup)


# In[ ]:





# In[4]:


soup.find_all("table")[1]


# In[ ]:





# In[5]:


soup.find("table" , class_ = "wikitable sortable")


# In[ ]:





# In[6]:


table = soup.find_all("table")[1]


# In[7]:


print(table)


# In[ ]:





# In[8]:


world_titles = table.find_all("th")


# In[9]:


world_titles


# In[ ]:





# In[10]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[ ]:





# In[11]:


import pandas as pd


# In[12]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[ ]:





# In[13]:


column_data = table.find_all("tr")


# In[14]:


for row in column_data[1:]:
    
    row_data = row.find_all("td")
    ind_row_data = [data.text.strip() for data in row_data]
    print(ind_row_data)
    
    length = len(df)
    df.loc[length] = ind_row_data


# In[ ]:





# In[15]:


df


# In[ ]:





# In[16]:


df.to_csv(r"C:\Users\Shafiq\~ProjectData\Outputs\RankedRevenue.csv" , index = False)


# In[ ]:




