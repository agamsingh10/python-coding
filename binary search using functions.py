#!/usr/bin/env python
# coding: utf-8

# In[9]:


def bsearch(n, num):
    beg=0
    end=n-1
    while beg<=end:
        mid=(beg+end)//2
        
        if a[mid]==num:
            flag=0
            break
        elif num>a[mid]:
            beg=mid+1
            flag=1
        elif num<a[mid]:
            end=mid-1
            flag=1
    if flag==1:
        print("not found")
    else:
            print("found")
a=eval(input("enter list"))
n=len(a)
num=int(input("enter number to be found"))
bsearch(n,num)


# In[12]:


def bsearch(n, num):
    beg=0
    end=n-1
    while beg<=end:
        mid=(beg+end)//2
        
        if a[mid]==num:
            flag=0
            break
        elif num>a[mid]:
            beg=mid+1
            flag=1
        elif num<a[mid]:
            end=mid-1
            flag=1
    return flag
a=eval(input("enter list"))
n=len(a)
num=int(input("enter number to be found"))
f=bsearch(n,num)
if f==1:
    print("not found")
else:
    print("found")


# In[ ]:




