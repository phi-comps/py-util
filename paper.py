
# coding: utf-8

# In[1]:


from util import *
import sympy as sy
from sympy import Rational
sy.init_printing()


# In[2]:


f_it(3).subs(xg, x - gamma)


# In[3]:


f_it(3).factor().subs(xg, x - gamma)


# In[24]:


f_it(3).subs(gamma, Rational(1,2)).subs(m, -Rational(7,4)).factor()


# In[11]:


f_it(1).subs(xg, x - gamma).subs(gamma, Rational(1,2)).subs(m, -Rational(7,4)).expand()


# In[6]:


Rational(1,2)

