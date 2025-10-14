#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


data = pd.read_csv("data\Advertising.csv")
data


# pd.read_csv() reads a CSV file into a pandas DataFrame, which is like an Excel sheet in Python.
# 
# r"..." means a raw string, used to handle backslashes in file paths.

# In[13]:


data.isnull().sum()


# isnull() checks for missing (NaN) values.
# 
# sum() counts how many missing values are in each column.
# 👉 Helps ensure data quality before training the model.

# In[15]:


X = data.iloc[:,1:2].values
y = data.iloc[:,4].values


# .iloc = index-based selection
# 
# [:, 1:2] means → all rows (:) and only column at index 1 (2nd column), kept as 2D array.
# 
# [:, 4] means → all rows, and only the 5th column as a 1D array.
# 
# values converts DataFrame to NumPy array (used by machine learning libraries).
# 
# Example:
# 
# If the dataset columns are:
# | TV | Radio | Newspaper | Sales |
# Then:
# 
# X = TV column (input)
# 
# y = Sales column (output)

# In[17]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .25, random_state = 1)


# The goal is to train the model on some data and test it on unseen data.
# 
# train_test_split() divides data into:
# 
# Training set (75%)
# 
# Testing set (25%)
# 
# random_state=1 ensures the same random split each time (for reproducibility).(copied data)

# In[19]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_test,y_test)


# We import LinearRegression from sklearn.linear_model.
# 
# reg = LinearRegression() creates an empty model.
# 
# .fit(X_train, y_train) trains (fits) the model on training data.
# 
# Under the hood:
# 
# The model learns a line of best fit:
# 
# y = b0 + b1x

# In[21]:


y_pred = reg.predict(X_test) #.predict() uses the trained model to predict y for unseen X_test values.


# In[23]:


reg.score(X_train,y_train)
reg.score(X_test,y_test)


# .score() returns the R² score (Coefficient of Determination):
# 
# 𝑅^2 = 1-SSR/SST
# 
# It measures how well the model fits the data.
# 
# Range:
# 
# 1.0 = perfect prediction
# 
# 0 = no predictive power
# 
# Higher R² → better model.
# 
# in above example r^2 is 0.5, it means model is not good

# In[25]:


print(reg.coef_)
print(reg.intercept_)


# In[28]:


X = 80
y1 = reg.intercept_ + reg.coef_ * X
y1
# y = c + mx


# In[31]:


plt.scatter(X_train, y_train, color='green') #plt.scatter() plots actual data points (green dots).
plt.plot(X_train, reg.predict(X_train), color='blue') #plt.plot() draws the regression line (blue line).
plt.title('TV Advertising')
plt.xlabel('TV')
plt.ylabel('Sales')


# The plot indicates that increasing TV advertising leads to higher sales, and the linear regression model fits the trend quite well, making TV advertising a strong predictor of sales performance.

# In[ ]:




