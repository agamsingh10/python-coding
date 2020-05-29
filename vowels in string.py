#!/usr/bin/env python
# coding: utf-8

# In[3]:


ch=input("enter string")
count=int(0)
n=len(ch)
for i in range(-1,-n-1,-1):
    if ch[i]=='a' or ch[i]=='e' or ch[i]=='i' or ch[i]=='o' or ch[i]=='u':
        count=count+1
print(count)        


# In[4]:


ch=input("enter string")
count=int(0)
n=len(ch)
for i in range(0,n):
    if ch[i]=='a' or ch[i]=='e' or ch[i]=='i' or ch[i]=='o' or ch[i]=='u':
        count=count+1
print(count) 


# In[ ]:




