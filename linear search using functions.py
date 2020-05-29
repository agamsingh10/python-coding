#!/usr/bin/env python
# coding: utf-8

# In[6]:


def lsearch(n, num):
    for i in range(n):
        if a[i]==num:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        print("not found")
    else:
            print("found")
a=eval(input("enter list"))
n=len(a)
num=int(input("enter number to be found"))
lsearch(n,num)


# In[5]:


def lsearch(n, num):
    for i in range(n):
        if a[i]==num:
            flag=0
            break
        else:
            flag=1
    return flag
a=eval(input("enter list"))
n=len(a)
num=int(input("enter number to be found"))
f=lsearch(n,num)
if f==1:
    print("not found")
else:
    print("found")


# In[ ]:




