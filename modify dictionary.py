#!/usr/bin/env python
# coding: utf-8

# In[1]:


course={'bca':3,'btech':4,'mca':1}
print(course)
course['bca']=8
print(course)


# In[2]:


course={'bca':3,'btech':4,'mca':1}
print(course)
for s in course:
    course[s]=9
print(course)    


# In[5]:


course={'bca':3,'btech':4,'mca':1}
print(course)
del course['mca']
print(course)


# In[9]:


course={'bca':3,'btech':4,'mca':1}
print(course)
del course['btech']
print(course)


# In[ ]:




