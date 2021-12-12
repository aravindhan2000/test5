#!/usr/bin/env python
# coding: utf-8

# In[102]:


class power():
    def pow(self, x, n):
        self.x=x
        self.n=n
        
        if x==1 or x==0 or n==1:
            return x
        
        if x==-1 and n==0:
            return -1
        
        if x>0:
            if n>1:
                return x**n
        
        if n==0:
            return 1
        
        if n<0:
            return 1/self.pow(x,-n)
        
        x=self.pow(x,n//2)
        
        if n%2==0:
            return x1*x1
        return x1**2*x
        
print(power().pow(10,2))


# In[ ]:




