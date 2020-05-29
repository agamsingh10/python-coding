#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add():
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a+b
    print(c)
add()
add()
print("gabs")
add()
print("yayaa")
add()
    
    


# In[3]:


def add(a,b):
    c=a+b
    print(c)
add(100,23)
add(23,24)
print("gabs")
add(24,67)
print("yayaa")
add(24,24)


# In[5]:


def add(a,b):
    c=a+b
    print(c)
    return c
k=add(100,23)
k=k+65
print(k)


# In[ ]:




