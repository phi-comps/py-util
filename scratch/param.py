
# coding: utf-8

# In[1]:


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


# In[2]:


M_ = 4*m+d**2+2
qqq = M**2+(d**4-4*d**2-4)
assert qq == qqq.subs(M, M_).expand()
eq = Eq(y**2, qqq)
eq


# In[3]:


m_ = solve(Eq(0,(eq.rhs-(M+r)**2).subs(M, M_).expand()), m)[0].expand().simplify()
m_


# In[4]:


def mat(r_, d_):
    return m_.subs(r, r_).subs(d, d_)

y_ = (d**4-4*d**2+r**2-4)/(2*r)
def yat(r_, d_):
    return y_.subs(r, r_).subs(d, d_)


# In[5]:


mat(-1, -1)


# In[6]:


mat(-2, 2)


# In[7]:


qq.subs(m, Rational(1,4)).subs(d, -1)


# In[8]:


tt_ = gamma + m + m**2
ss_ = -2*m + 2*t


# In[9]:


#f^2 newly red iff (1/4)ss_^4+mss_^2=Y^2
((((ss_**4/4+m*ss_**2).expand().subs(t**2, tt_).subs(t**3, t*tt_).subs(gamma, gamma_nice.subs(beta, y)).subs(m, m_).subs(y, y_)).expand()))


# In[10]:


gammma = gamma_nice.subs(beta, y_).subs(m, m_)
gammma


# In[11]:


first = (-m_-gammma)
second = tt_.subs(gamma, gammma).subs(m, m_)


# In[12]:


(256*r**2*first).expand().factor()


# In[13]:


foo = (256*r**2*second).expand().factor()
foo


# In[53]:


scnd = (-foo.as_two_terms()[1].as_two_terms()[1])
scnd


# In[15]:


(first.subs(d, d)*256*r**2).expand()


# In[16]:


(second.subs(d, d)*256*r**2).expand()


# In[18]:


(second.subs(r, 1)).expand()


# In[19]:


(second.subs(d, 2)).expand()


# In[20]:


(second*256*r**2).expand().coeff(r, n=0).factor()


# In[21]:


(second*256*r**2).expand().coeff(d, n=0).factor()


# In[22]:


(first*256*r**2).expand().as_poly(r)


# In[23]:


(second*256*r**2).expand().as_poly(r)


# In[24]:


tuple(map(lambda x: x.evalf(), solve((second*256*r**2).subs(d, 2).expand(), r)))


# In[25]:


tuple(map(lambda x: x.evalf(), solve((first).subs(d, 2).expand(), r)))


# In[26]:


(second*256*r**2).factor()


# In[27]:


meat = (second*256*r**2).factor().as_two_terms()[1].as_two_terms()[1]
meat


# In[28]:


def is_real(x):
    return x.as_real_imag()[1] == 0

def rroots(P):
    return sorted(tuple(filter(is_real, map(lambda x: x.evalf(), solve(P, r)))))

def this_is_not_satisfying(d_):
    fst = rroots(first.subs(d, d_))
    snd = rroots(meat.subs(d, d_))
    if len(fst)%2==1 and len(snd)%2==1:
        return snd[-1] < fst[-2]


# In[32]:


d__ = False
for d_ in range(1000):
    if this_is_not_satisfying(d_):
        display(d_)
        d__ = d_


# In[34]:


d__


# In[ ]:


x.as_real_imag()


# In[ ]:


display(Latex(5))


# In[37]:


fst = (first*256*r**2).expand()
fst


# In[38]:


snd = (second*256*r**2).expand()
snd


# In[46]:


fst


# In[54]:


scnd


# In[52]:


fst.subs(r, x**4)


# In[55]:


fst.factor()


# In[64]:


frst = fst.factor().as_two_terms()[1].as_two_terms()[1]
frst


# In[73]:


frst


# In[74]:


scnd


# In[78]:


frst.subs(r, -d**2)


# In[79]:


scnd.subs(r, -d**2)


# In[81]:


fst.factor()

