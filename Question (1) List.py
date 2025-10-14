#!/usr/bin/env python
# coding: utf-8

# 1. Create a list of 5 integers. Perform and print the result of the following operations:
#    append, extend, insert, remove, pop, clear, index, count, sort, and reverse.

# In[83]:


the_list = [2,3,4,6,7]
the_list


# In[84]:


# Append operation
the_list.append(9)
the_list


# In[85]:


# Extend Operation
my_list = [1,5]
my_list


# In[86]:


the_list.extend(my_list)
the_list


# In[87]:


the_list.insert(3,10)
the_list


# In[88]:


the_list.remove(4)
the_list


# In[89]:


the_list.pop()
the_list


# In[90]:


the_list[0]


# In[91]:


the_list[1:4]


# In[92]:


the_list.count(3)


# In[93]:


the_list.sort()


# In[94]:


the_list


# In[95]:


the_list.reverse()


# In[96]:


the_list


# In[98]:


the_list.clear()
the_list


#  2. Create a tuple that stores 3 student names. 
#  Try changing the second name in the tuple. What happens? Explain why.

# In[99]:


students = ("Sukhada", "Shweta", "Parth")
print(students)


# In[100]:


students[1] = 'Sarvesh' 


# # Explanation
# 
# - Tuples are immutable in Python.
# - That means once a tuple is created, you cannot change, add, or remove elements directly.
# - Trying to modify any element will result in a TypeError.

# In[101]:


# convert tuple to list
temp_list = list(students)
temp_list[1] = 'Sarvesh'
students = tuple(temp_list)
print(students)


# In[102]:


print(type(list))


# In[ ]:




