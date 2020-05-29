#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=eval(input("enter a list"))
n=len(a)
num=int(input("a number to find"))
for i in range(0,n):
            if num==a[i]:
                flag=1
                break
            else:
                flag=0
if flag==0:
    print("not found")
else:
    print("found")
            
    


# In[ ]:




