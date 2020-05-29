#!/usr/bin/env python
# coding: utf-8

# In[19]:


for i in range(1,101):
        if i==2:
            print(i)
        else:
            for k in range(2,i):
                if i%k==0:
                    flag=1
                    break
                else:
                    flag=0
            if flag==0:
                print(i)
        
            


# In[ ]:





# In[ ]:




