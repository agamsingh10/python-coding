#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=eval(input("enter"))
n=len(a)
for i in range(0,n):
    m=a[i]
    for x in range(i+1,n):
        if m==a[x]:
            flag=1
            break
        else:
            flag=0
    if flag==1:
         
        for j in range(i-1,-1,-1):
            if m==a[j]:
                flag=0
                break
            else:
                flag=1
    if flag==1:
        print(a[i])
        
            


# In[ ]:




