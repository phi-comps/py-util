
# coding: utf-8

# In[7]:


# import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma, kappa
from IPython.display import display, Latex

from util import *
from transform import *

f_ = xg**3+a*xg+m+gamma
f = f_.subs(xg, x-gamma)
ff = f_.subs(xg, f_-gamma).expand().subs(xg,x)
p = ff.as_poly(x)
p


# In[34]:


q.subs(a,2*m).factor()


# In[37]:


ff.subs(a,2*m).simplify()


# In[38]:


def delta(var):
    return sqrt(-3*var**2-4*a)


# In[42]:


def r_p(var):
    return (-var+delta(var))/2
def r_m(var):
    return (-var-delta(var))/2


# In[46]:


for subscript in range(10):
    globals()['b{}'.format(subscript)] = Symbol('beta{}'.format(subscript))


# In[64]:


fact1=(x-r_p(b1))*(x-r_p(b2))*(x-r_p(b3))
fact2=(x-r_m(b1))*(x-r_m(b2))*(x-r_m(b3))


# In[68]:


(fact1.expand()-fact2.expand()).as_poly(x)


# In[69]:


(fact1.expand()-fact2.expand()).as_poly(x).coeffs()


# In[74]:


(fact1.expand()+fact2.expand()).as_poly(x).coeffs()


# In[76]:


fact3=(x-r_m(b1))*(x-r_p(b2))*(x-r_p(b3))
fact4=(x-r_p(b1))*(x-r_m(b2))*(x-r_m(b3))
(fact3+fact4).expand().as_poly(x).coeffs()


# In[77]:


(fact3-fact4).expand().as_poly(x).coeffs()


# In[84]:


c1=fact1.expand().as_poly(x).coeffs()[-1]
c2=fact2.expand().as_poly(x).coeffs()[-1]


# In[85]:


c1


# In[86]:


c2


# In[88]:


c1+c2


# In[1]:


from mpmath import *


# In[8]:


polar(4*x)

