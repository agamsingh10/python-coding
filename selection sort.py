#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=eval(input("enter"))
n=len(a)
for j in range(n-1):
    small=a[j]
    pos=j
    for i in range(j+1,n):
        if small>a[i]:
            small=a[i]
            pos=i
    c=a[j]
    a[j]=a[pos]
    a[pos]=c
print(a)    


# In[ ]:




