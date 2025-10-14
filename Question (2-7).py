#!/usr/bin/env python
# coding: utf-8

# 2.Create a tuple that stores 3 student names. Try changing the second name in the tuple. What happens? Explain why

# In[1]:


students = ("Sukhada", "Shweta", "Parth")
print(students)


# In[2]:


students[1] = "Sarvesh"


# Explanation:
# - Tuples are immutable in Python.
# - That means once a tuple is created, you cannot change, add, or remove elements directly.
# - Trying to modify any element will result in a TypeError.

# In[5]:


temp_list = list(students)
temp_list[1] = "Sarvesh"
students = tuple(temp_list)
print(students)


# 3. Create a set of integers with some duplicate values. Print the set and explain the output.

# In[14]:


my_set = {1: 20, 2: 40, 3: 60, 4: 20, 5: 40, 6: 20, 7: 60}
my_set


# Explanation of Output
# 
# A dictionary in Python stores data as key: value pairs.
# 
# In your case:
# 
# - Keys = 1, 2, 3, 4, 5, 6, 7
# 
# - Values = 20, 40, 60, 20, 40, 20, 60
# 
# So the dictionary means:
# 
# - Key 1 maps to value 20
# 
# - Key 2 maps to value 40
# 
# - Key 3 maps to value 60
# 
# - Key 4 maps to value 20
# 
# - Key 5 maps to value 40
# 
# - Key 6 maps to value 20
# 
# - Key 7 maps to value 60

# 4. Create a dictionary with the keys: 'name', 'age', and 'city'. Update the age and add a new key 'email'. Print the final dictionary.

# In[17]:


detail = {"name":"Sukhada", "age": 22, "city": "Nanded"}
detail


# In[19]:


detail["age"] = 21
detail


# In[21]:


detail["email"] = "sk@gmail.com"


# In[22]:


print(detail)


# 5.Write a script that checks if a person is eligible to vote (age ≥ 18). Take age as a variable and print the appropriate message

# In[26]:


age = int(input("Enter Age:"))
if age>=18:
    print("Your are eligable for vote")
else:
    print("Your are not eligable for vote")
    


# 6.Given a 'marks' variable, print the grade:
# - 90 and above: 'A'
# - 75–89: 'B'
# - 50–74: 'C'
# - Below 50: 'Fail'

# In[1]:


marks = int(input("Enter Marks:"))
if marks>=90:
    print("A")
elif 75<=marks>=89:
    print("B")
elif 50<=marks>=74:
    print("C")
else:
    print("Fail")
    


# 7.Given a number, check if it's positive, and if it is also even. If not positive, print if it's zero or negative.

# In[3]:


n = int(input())
if n>0:
    if n%2==0:
        print(f"{n} is postive and even")
    else:
        print(f"{n} is postive but negative")
elif n==0:
    print(f"{n} is zero")
else:
    print(f"{n} is negative")
    


# In[ ]:




