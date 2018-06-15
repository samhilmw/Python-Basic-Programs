
# coding: utf-8

# ### Basic operations with Numbers and their reversed forms

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


a = np.arange(-100,101,1)


# In[3]:


b = np.arange(-100,101,1)
for i in range(0,201):
    sum = int(0)
    while(b[i]!=0):
        sum = sum*10 +int(b[i]%10)
        b[i] = int(b[i]/10)
    b[i] = sum
        


# In[4]:


for i in range(0,101):
    b[100-i] = (-1)*b[100+i]


# In[5]:


print(a,b,sep="\n\n")


# In[6]:


plt.plot(a,a-b)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Fn")
plt.show()


# In[7]:


plt.plot(a,b-a)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Fn")
plt.show()


# In[8]:


plt.plot(a,a+b)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Fn")
plt.show()

