#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=int(input("enter"))
b=int(input("enter"))
if a%2==0 and b%2==0:
    num=(b-a)/2+1
elif a%2!=0 and b%2!=0:
    num=(b-a)/2
elif    a%2!=0 and b%2==0:
    num=int((b-a)/2+1)
elif    a%2==0 and b%2!=0:
    num=int((b-a)/2+1)
print("num of even num are",num)
    


# In[ ]:





# In[ ]:




