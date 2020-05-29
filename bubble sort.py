#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=eval(input("enter"))
n=len(a)
for j in range(n-2,-1,-1):
    for i in range(n-1):
        if a[i]>a[i+1]:
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
print(a)   


# In[ ]:




