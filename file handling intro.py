#!/usr/bin/env python
# coding: utf-8

# In[1]:


ch=input("enter a word")
fw=open("gabs.txt","w")
fw.write(ch)
fw.close()


# In[8]:


fr=open("gabs.txt","r")
ch=fr.read(11)
print(ch)
fr.close()


# In[5]:


a=int(input("enter a number"))
fw=open("abc.txt","w")
fw.write(str(a))
fw.close()


# In[7]:


fr=open("abc.txt","r")
ch=fr.read(6)
print(ch)
fr.close()


# In[10]:


fr=open("gabs.txt","r")
ch=fr.read(1)
ch2=fr.read(3)
print(ch)
print(ch2)
fr.close()


# In[ ]:




