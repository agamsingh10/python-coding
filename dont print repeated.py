#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ch=input("enter")
n=len(ch)
for i in range(n):
    m=ch[i]
    for x in range(i+1,n+1):
        if x==n:
            flag=1
            
        elif m==ch[x]:
            flag=0
            break

        else:
            flag=1          
    if flag==1:
        for j in range(i-1,-1,-1):
            if m==ch[j]:
                flag=0
                break
            else:
                flag=1
    if flag==1:
        print(ch[i])
        


# In[8]:


ch="gabs"
for i in range(4):
    m=ch[i]
    print(m)


# 
