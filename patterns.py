#!/usr/bin/env python
# coding: utf-8

# In[25]:


for k in range(2, 15, 4):
    print()
    for i in range(1, k, 2):
        print(i, end=' ')

for j in range(8, 1, -2):
    print()
    for p in range(1, j, 2):
        print(p, end=' ')

# In[40]:


k = 2
for j in range(5, 0, -1):
    for i in range(1, j):
        print(" ", end='')
    for p in range(1, k):
        print(p, end='')
    print()
    k = k + 1

# In[42]:


k = 1
l = 10
for j in range(1, 4):
    for i in range(1, 6):
        print(j, end=' ')
    print()
    for i in range(k, l, 2):
        print(i, end=' ')
    print()
    k = k + 10
    l = l + 10

# In[43]:


l = 95
m = 1
n = 6
for k in range(100, 89, -5):
    for i in range(k, l, -1):
        print(i, end=' ')
    print()
    for i in range(m, n):
        print(i, end=' ')
    print()
    l = l - 5
    m = m + 5
    n = n + 5

# In[44]:


for k in range(2, 7):
    for i in range(1, k):
        print(i, end='')
    print()

# In[45]:


for k in range(2, 6):
    for i in range(1, k):
        print("*", end='')
    print()

# In[ ]:




