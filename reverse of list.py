#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=eval(input("enter a list"))
n=len(a)
i=n-1
for j in range(0,n):
    if j>i:
        break
    else:
        c=a[i]
        a[i]=a[j]
        a[j]=c
    i=i-1 
print(a)    


# In[ ]:




