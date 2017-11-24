
# coding: utf-8

# In[1]:


import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, e, f, g, h, m, x, y, alpha, beta, gamma

from IPython.display import display, Latex

from util import *
from transform import *
from ec import EllipticCurve, Point

__all__ = [
    'gammas_at',
    'gammas',
    'gamma_nice',
    'gamma',
    'beta',
    'beta_',
    'aa_',
    'bb_',
    'qq',
    'factor',
    'check_newly',
    'up55',
    'lo55',
    'nice',
    ]

for subscript in range(10):
    for var in 'abcdefgh':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)

def displ(*x):
    if __name__ == '__main__':
        display(*x)

def show(eqs):
    displ(Latex('\n'.join(
        [r'\begin{align}']
        + list(r'{} &= {} \\'.format(sy.latex(eq.lhs), sy.latex(eq.rhs)) for eq in eqs)
        + [r'\end{align}']
    )))


def mk_p(n, var, alt=False):
    assert n > 0
    cs = iter(sy.symbols(' '.join(string.ascii_lowercase)))
    p = 0
    for i in range(n):
        t = next(cs)*var**i
        if alt and i%2:
            t = -t
        p += t
    return p + var**n


# In[2]:


p1_ = mk_p(8, xg)
p1_


# In[3]:


p2_ = mk_p(8, xg, alt=True)
p2_


# In[4]:


eqs = nontriv(equate(f_it(4), p1_*p2_, xg))
show(eqs)


# In[6]:


eqs = nontriv(bigsubs(eqs, g, only(solve(eqs[-1], g))))
show(eqs)


# In[7]:


eqs = nontriv(bigsubs(eqs, e, only(solve(eqs[-1], e))))
show(eqs)


# In[8]:


eqs = nontriv(bigsubs(eqs, c, only(solve(eqs[-1], c))))
show(eqs)


# In[9]:


eqs = nontriv(bigsubs(eqs, a, only(solve(eqs[-1], a))))
show(eqs)


# In[10]:


show(Eq(e.lhs, e.rhs.expand()) for e in eqs)


# In[20]:


solve(eqs[-1], d)

