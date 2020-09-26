#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 
import numpy as np


# In[8]:


# step1->population initialization 
pop=np.empty((6,8),dtype=np.int32)
for i in range(6):
    for j in range(8):
        pop[i][j]=random.randint(0,1)
    
print(pop)


# In[11]:


#step2->fitness function
f=[]
for i in pop:
    j=list(i)
    f.append(j.count(1))
print(f)


# In[12]:


#step3->parent selection
c_p=[]
f_c=f.copy()
for i in range(2):
    c_p.append(np.argmax(f_c))
    f_c[np.argmax(f_c)]=0
print(c_p)


# In[21]:


#step4->crossover
parent1=pop[c_p[0],:]
parent2=pop[c_p[1],:]
child1=[]
child2=[]
parent1, parent2 
for i in range(len(parent1)):
    if(i<3):
        child1.append(parent1[i])
    else:
        child1.append(parent2[i])
for i in range(len(parent1)):
    if(i<3):
        child2.append(parent2[i])
    else:
        child2.append(parent1[i])
child1, child2


# In[ ]:




