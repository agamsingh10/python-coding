#!/usr/bin/env python
# coding: utf-8

# In[7]:


ch=input("enter string")
n=len(ch)
i=n-1
for j in range(0,n):
    if j>i:
        break
    if ch[i]==ch[j]:
        flag=1
    else:
        flag=0
        break
    i=i-1
    
if flag==1:
    print("it is pallindrome")
else:
    print("not pallindrome")


# In[10]:


ch=input("enter string")
n=len(ch)
i=-n
for j in range(-1,-n-1,-1):
    if i>j:
        break
    if ch[i]==ch[j]:
        flag=1
    else:
        flag=0
        break
    i=i+1
    
if flag==1:
    print("it is pallindrome")
else:
    print("not pallindrome")


# In[ ]:




