#!/usr/bin/env python
# coding: utf-8

# In[12]:


n=int(input("enter the number"))
if n==2:
    print("prime")
else:
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
           print("prime")
    elif flag==1:
           print("not prime")
            


# In[ ]:





# In[ ]:




