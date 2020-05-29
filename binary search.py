#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=eval(input("enter a list"))
n=len(a)
num=int(input("a number to find"))
beg=0
end=n-1
for beg in range(0,end+1):
        mid=(beg+end)//2    
        if num==a[mid]:
                flag=1
                break
        elif num<a[mid]:
            end=mid-1
            flag=0
        elif num>a[mid]:
            beg=mid+1
            flag=0
            
if flag==0:
    print("not found")
else:
    print("found")
            
    


# In[ ]:





# In[ ]:




