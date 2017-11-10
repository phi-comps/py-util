
# coding: utf-8

# In[1]:


import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma

from IPython.display import display, Latex

from util import *
from transform import *
from points import *
from ec import EllipticCurve, Point


# In[2]:


lo55


# In[3]:


up55


# In[4]:


up55.as_poly(b)


# In[5]:


b_ = solve(Eq(0, lo55), b)[1].subs(sqrt(qq), beta)
b_


# In[6]:


up55.subs(b, b_).expand().as_poly(beta).as_expr()


# In[7]:


(x**4+6*x**3+11*x**2+6*x+1).factor()


# In[8]:


(x**4+6*x**3+11*x**2+5*x).factor()


# In[9]:


nice


# In[10]:


solve(nice[1], b)


# In[11]:


solve(nice[1], b)[1].subs(c, solve(nice[3], c)[0])


# In[12]:


solve(nice[1], b)[1].subs(c, solve(nice[3], c)[0]).subs(a, solve(nice[2], a)[0])


# In[13]:


solve(nice[1], b)[1].subs(c, solve(nice[3], c)[0]).subs(a, solve(nice[2], a)[0])**2


# In[14]:


(solve(nice[1], b)[1].subs(c, solve(nice[3], c)[0]).subs(a, solve(nice[2], a)[0])**2).expand()


# In[15]:


nice


# In[16]:


nicee = [e.subs(c, solve(nice[3], c)[0]) for e in nice[:-1]]
nicee


# In[36]:


niceee = [e.subs(a, solve(nicee[2], a)[0]) for e in nicee[:-1]]
display(niceee[0])
display(niceee[1])


# In[18]:


Eq(niceee[0].lhs - niceee[1].lhs, niceee[0].rhs - niceee[1].rhs)


# In[19]:


((niceee[0].lhs-niceee[0].rhs).expand() - gamma - m).factor()


# In[20]:


hi = (niceee[0].lhs-niceee[0].rhs).expand()
hi


# In[21]:


lo = ((niceee[1].lhs-niceee[1].rhs).expand())
lo


# In[22]:


(m*lo).expand()


# In[23]:


((hi + 2*m*lo).expand())


# In[24]:


nice


# In[25]:


solve(nice[1], b)[1]


# In[26]:


solve(hi, b)


# In[27]:


b_ = solve(hi, b)[1].subs(sqrt(nice[0].lhs), a)
b_


# In[37]:


(lo.subs(b, b_).expand()*d**2*1).expand()


# In[35]:


[(lo.subs(b, b_).expand()*d**2*1).expand().coeff(d, n=i) for i in [8 ,6, 4, 2, 0]]


# In[39]:


qq.subs(d, 1).subs(m, -Rational(15, 8))

