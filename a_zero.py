
# coding: utf-8

# In[4]:


import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma

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

def displ(*x):
    if __name__ == '__main__':
        display(*x)

def show(eqs):
    display(Latex('\n'.join(
        [r'\begin{align}']
        + list(r'{} &= {} \\'.format(sy.latex(eq.lhs), sy.latex(eq.rhs)) for eq in eqs)
        + [r'\end{align}']
    )))


# In[9]:


displ(aa_)
l, r = solve(Eq(0, aa_), m)
l, r


# In[3]:


C, xtrans, ytrans = transform(4, 0, 8, 0, -2, 0)
C, xtrans, ytrans


# In[15]:


def wat(C):
    for x in C:
        yield int(x), 1

eclib.mwrank(wat(C))

