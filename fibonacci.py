#!/usr/bin/env python
# coding: utf-8

# In[18]:


for k in range(1,6):
       print("\n")
       for i in range(1,k):
            print(i, end='')


# In[9]:


for i in range(1,3):
    print("$", end='')


# In[20]:


a=int(input("enter a number"))
for i in range(1,11):
    print(a*i)


# In[27]:


n=int(input("enter how long fibonacci you want"))
a=int(0)
b=int(1)
print(a,b,end=' ')
for i in range(n-2):
      c=a+b
      print(c,end=' ')
      a=b
      b=c


# In[ ]:




