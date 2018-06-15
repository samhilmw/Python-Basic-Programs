
# coding: utf-8

# ### Diamond Pattern

# In[1]:


n = int(input("Enter Number of Rows: "))

for i in range(0,n):
    for j in range(0,n):
        if(j<n-i):
            print(" ",end='')
    for j in range(0,i+1):
        print("* ",end='')
    print('\n')
for i in range(0,n):
    for j in range(0,i+2):
        print(' ',end="")
    for j in range(0,n-i-1):
        print('* ',end="")
    print('\n')

