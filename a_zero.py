
# coding: utf-8

# In[43]:


import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma, kappa

from IPython.display import display, Latex

from util import *
from transform import *
from points import *
from ec import EllipticCurve, Point
import eclib


for subscript in range(5):
    for var in 'abcdefgh':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)

def ds(*x):
    if __name__ == '__main__':
        display(*x)

def show(eqs):
    display(Latex('\n'.join(
        [r'\begin{align}']
        + list(r'{} &= {} \\'.format(sy.latex(eq.lhs), sy.latex(eq.rhs)) for eq in eqs)
        + [r'\end{align}']
    )))


# In[44]:


ds(aa_)
l, r = solve(Eq(0, aa_), m)
l, r


# In[45]:


kk_ = -2*d**4 + 8*d**2 + 4
m_ = r.subs(sqrt(kk_), kappa)
bb_.subs(m, m_)


# In[66]:


ds(Eq(gamma, aa_*beta + bb_))
ds(Eq(0, aa_))
ds(Eq(gamma, bb_))
aa__ = (-aa_/d**2).expand()
ds((Eq(d, 0), Eq(0, aa__)))
ds(Eq(-gamma-m, -bb_-m))
ds(((-bb_-m)-4*m*aa_).expand())
ds((((-bb_-m)-4*m*aa_).expand()/d**4).expand())
ds((((-bb_-m)-4*m*aa_).expand()/d**4).expand() + 7*aa__/2)
ds(((((-bb_-m)-4*m*aa_).expand()/d**4).expand() + 7*aa__/2).factor())


# In[35]:


(-((-bb_-m-4*aa_*m).expand()*-64/(d**4) + 14*((4*aa_/d**2).expand()*4).expand()).expand()).factor()


# In[28]:


((4*aa_/d**2).expand()*4).expand()


# ## Curve for $\kappa$

# In[3]:


C, xtrans, ytrans = transform(4, 0, 8, 0, -2, 0)
C, xtrans, ytrans


# In[15]:


def wat(C):
    for x in C:
        yield int(x), 1

eclib.mwrank(wat(C))

