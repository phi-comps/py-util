
# coding: utf-8

# In[2]:


import sys
sys.path.append('..')

import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, m, r, s, t, x, y, alpha, beta, gamma, M

from IPython.display import display, Latex

from util import *
from transform import *
from points import *
from ec import EllipticCurve, Point


# In[3]:


M_ = 4*m+d**2+2
qqq = M**2+(d**4-4*d**2-4)
assert qq == qqq.subs(M, M_).expand()
eq = Eq(y**2, qqq)
eq


# In[4]:


m_ = solve(Eq(0,(eq.rhs-(M+r)**2).subs(M, M_).expand()), m)[0].expand().simplify()
m_


# In[5]:


def mat(r_, d_):
    return m_.subs(r, r_).subs(d, d_)

y_ = (d**4-4*d**2+r**2-4)/(2*r)
def yat(r_, d_):
    return y_.subs(r, r_).subs(d, d_)


# In[6]:


mat(-1, -1)


# In[7]:


mat(-2, 2)


# In[8]:


qq.subs(m, Rational(1,4)).subs(d, -1)


# In[9]:


tt_ = gamma + m + m**2
ss_ = -2*m + 2*t


# In[10]:


#f^2 newly red iff (1/4)ss_^4+mss_^2=Y^2
((((ss_**4/4+m*ss_**2).expand().subs(t**2, tt_).subs(t**3, t*tt_).subs(gamma, gamma_nice.subs(beta, y)).subs(m, m_).subs(y, y_)).expand()))


# In[11]:


gammma = gamma_nice.subs(beta, y_).subs(m, m_)
gammma


# In[12]:


first = (-m_-gammma)
second = tt_.subs(gamma, gammma).subs(m, m_)


# In[20]:


(256*r**2*first).expand().factor()


# In[22]:


fst = (256*r**2*first).expand().factor().as_two_terms()[1].as_two_terms()[1]
fst


# In[23]:


(256*r**2*second).expand().factor()


# In[29]:


snd = -(256*r**2*second).expand().factor().as_two_terms()[1].as_two_terms()[1]
snd


# f^3 newly red iff fst and snd non-square
