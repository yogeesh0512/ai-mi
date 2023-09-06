#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import missingno as msno
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


titanic_df=pd.read_csv('C:\\Users\\GPT-INF014\\Downloads\\titanic1.csv')
titanic_df


# In[4]:


titanic_df.info()


# In[5]:


titanic_df.isnull()


# # using missingno to visualise missing values

# In[6]:


msno.bar(titanic_df)


# In[7]:


msno.matrix(titanic_df)


# # deleting the entire row

# In[8]:


titanic_df.isnull().sum()


# In[9]:


df = titanic_df.dropna(axis=0)
df.isnull().sum()


# In[10]:


df.info()


# # deleting the entire column

# In[11]:


titanic_df.columns


# In[13]:


df = titanic_df.drop(['deck'],axis=1)
df.isnull().sum()


# # imputing the missing value

# # replacing with artibatry value

# In[14]:


titanic_df['deck'].unique()


# In[15]:


titanic_df['deck']=titanic_df['deck'].fillna('c')


# In[16]:


titanic_df['deck'].isnull().sum()


# In[17]:


titanic_df


# # replacing with mean

# In[18]:


mean = titanic_df['age'].mean()
print(mean)
titanic_df['age'] = titanic_df['age'].fillna(mean)
titanic_df['age']


# # replacing with mode

# In[19]:


titanic_df = pd.read_csv('C:\\Users\\GPT-INF014\\Downloads\\titanic1.csv')
mode = titanic_df['deck'].mode()[0]
print(mode)
titanic_df['deck'] = titanic_df['deck'].fillna(mode)


# In[20]:


titanic_df['deck']


# # replacing with median

# In[22]:


titanic_df['age']= titanic_df['age'].fillna(titanic_df['age']).median()
titanic_df['age']


# # forword and backword filliing of missing values

# In[31]:


titanic_df = pd.read_csv('C:\\Users\\GPT-INF014\\Downloads\\titanic2.csv')
titanic_df


# In[32]:


new_df = titanic_df.fillna(method='ffill')
new_df


# In[36]:


new_df = titanic_df.fillna(method="ffill",limit=1)
new_df


# In[37]:


new_df = titanic_df.fillna(method="bfill",limit=1)
new_df


# In[ ]:




