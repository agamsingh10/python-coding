#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=eval(input("enter a list"))
n=len(a)
i=0
while i<n:
    m=a[i]
    for x in range(i+1,n):
        
            if m==a[x]:
                k=a[x]
                b=a.count(m)
                for j in range(b):
                            a.remove(m)
                n=n-b
                break
            
    if m==k:
        i=0
    else:
        i=i+1
print(a)                
        


# In[ ]:




