#!/usr/bin/env python
# coding: utf-8

# 8.Create:
# - A scalar using np.array(5)
# - A 1D array with values 1 to 5
# - A 2D array (2x3) with values from 10 to 60 in steps of 10
# 

# In[1]:


import numpy as np


# In[2]:


a = np.array(5)


# In[4]:


a = np.array([1,2,3,4,5])
a


# In[6]:


a = np.arange(1,6)
a


# In[10]:


a = np.array([[10,20,30], [40,50,60]])
a


# In[11]:


a = np.arange(10,70,10).reshape(2,3)
a


# 9. Generate a 4x4 Numpy array of random integers between 0 and 100 using np.random.randint().

# In[12]:


import random


# In[17]:


arr = np.random.randint(0,100,size=(4,4))
print(arr)


# 10.	Create a 2D numpy array of shape (3x3). Convert it into a pandas DataFrame and add column names: 'A', 'B', 'C'.

# In[18]:


import pandas as pd

b = np.array([[2,3,5],[6,7,8],[4,9,1]])
b


# In[19]:


df = pd.DataFrame(b,columns=['A','B','C'])
df


# # Section C: 
#  Exploring Pandas

# 11.	Create a small DataFrame manually with 10 rows and columns: 'Name', 'Age', 'City', and 'Salary'. Then:
# - Use .info(), .describe()
# - Select 'Name' and 'City' columns
# - Drop 'City' column
# - Fill any missing values in 'Salary' column with the mean
# - Remove any duplicate rows
# 

# In[48]:


import pandas as pd

data = {
    'Name': ['Sukhada','Shweta','Atharva','Parth','Piyush','Sarvesh','Ananya','Smita','Akshya','Zoha'],
    'Age': [22,25,22,20,27,24,22,32,29,21],
    'City': ['Dehli','Bangalore','Mumbai','Pune','Nashik','Nagpur','Pune','Mumbai','Bangalore','Dehli'],
    'Salary': [65000, 66000, 67000, 43000, 60000, 47000, 55000, 44000, 69000, 58000]
}

df = pd.DataFrame(data)
print(df)


# In[49]:


df.info()


# In[50]:


df.describe()


# In[51]:


Selecte_column = df[['Name','City']]
print(Selecte_column)


# In[52]:


drop_data=df.drop('City',axis=1)
drop_data


# In[59]:


# Sample DataFrame with a missing value

data = {
    'Name': ['Sukhada','Shweta','Atharva','Parth','Piyush','Sarvesh','Ananya','Smita','Akshya','Zoha'],
    'Age': [22,25,22,20,27,24,22,32,29,21],
    'City': ['Dehli','Bangalore','Mumbai','Pune','Nashik','Nagpur','Pune','Mumbai','Bangalore','Dehli'],
    'Salary': [65000, 66000, 67000, None, 60000, 47000, 55000, 44000, 69000, 58000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Fill missing values in 'Salary' with the mean
mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)
print("\nDataFrame after filling missing Salary with mean:")

print(df)


# In[ ]:





# In[ ]:




