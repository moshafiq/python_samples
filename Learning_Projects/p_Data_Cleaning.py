#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"Z:\Shafiq\Certifications\~Tech\~Learning\Python\pandas\data\Customer Call List.xlsx")
df


# In[3]:


df = df.drop(columns = "Not_Useful_Column")
df


# In[4]:


df


# In[5]:


df["Last_Name"]


# In[6]:


df["Last_Name"] = df["Last_Name"].str.strip("./_")
df["Last_Name"]


# In[7]:


df


# In[8]:


df["Phone_Number"]


# In[9]:


df["Phone_Number"] = df["Phone_Number"].str.replace("[^a-zA-Z0-9]","")
df["Phone_Number"]


# In[ ]:





# In[10]:


df["Phone_Number"] = df["Phone_Number"].apply (lambda x: str(x))
df["Phone_Number"]


# In[11]:


df["Phone_Number"] = df["Phone_Number"].apply (lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])
df


# In[ ]:





# In[12]:


df["Phone_Number"] = df["Phone_Number"].str.replace("[^0-9]","")
df["Phone_Number"]


# In[13]:


df


# In[ ]:





# In[14]:


df["Address"]


# In[ ]:





# In[15]:


df[["Street","County/State","ZipCode"]] = df["Address"].str.split("," , 2 , expand=True)


# In[16]:


df


# In[17]:


df = df.drop(columns = "Address")
df


# In[18]:


df["Do_Not_Contact"]


# In[19]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes","Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No","N")
df["Do_Not_Contact"]


# In[ ]:





# In[20]:


df


# In[21]:


for x in df.index:
    print(x)


# In[22]:


for x in df.index: 
    if df["Do_Not_Contact"].loc[x] == "Y":
        df.drop(x, inplace=True)
        
df


# In[ ]:





# In[23]:


type(df["Do_Not_Contact"].loc[0])


# In[24]:


type(df["Do_Not_Contact"].loc[2])


# In[ ]:





# In[25]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].apply(lambda x: str(x))
df


# In[26]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("nan","N")


# In[27]:


df


# In[ ]:





# In[28]:


for x in df.index: 
    if df["Phone_Number"].loc[x] == "":
        df.drop(x, inplace=True)
        
df


# In[ ]:





# In[29]:


df = df.reset_index(drop=True)
df


# In[ ]:





# In[30]:


df = df.drop_duplicates()
df


# In[ ]:





# In[31]:


df["Paying Customer"] = df["Paying Customer"].str.replace("Yes","Y")
df["Paying Customer"] = df["Paying Customer"].str.replace("No","N")
df


# In[ ]:





# In[32]:


df


# In[ ]:




