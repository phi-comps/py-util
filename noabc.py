
# coding: utf-8

# In[1]:


import itertools

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


# In[2]:


def binseqs(n):
    if n == 0:
        yield ()
    else:
        for seq in binseqs(n - 1):
            yield seq + (0,)
            yield seq + (1,)

for n in range(4):
    for seq in binseqs(n):
        s = ''.join(map(str, seq))
        globals()['a_' + s] = Symbol('\\alpha_{' + s + '}')


# In[3]:


def mk_rt(*signs):
    acc = sqrt(m-gamma)
    for sign in reversed(signs):
        acc = sqrt(m + sign*acc)
    return acc


# In[4]:


mk_rt(1, -1, -1)


# In[19]:


p_ = (y + a_00)*(y + a*a_01)*(y + b*a_10)*(y + c*a_11)


# In[20]:


coeffs = [ coeff.expand() for coeff in p_.expand().as_poly(y).coeffs() ]
coeffs


# In[21]:


co = coeffs[1]


# In[22]:


co


# In[32]:


# def reps(pp_):
#     pp_.replace(mk_rt(1,1)*mk_rt(-1,1), sqrt(m**2-m-sqrt(m-gamma)))
#     pp_.replace(mk_rt(-1,1)*mk_rt(1,1), sqrt(m**2-m-sqrt(m-gamma)))
#     pp_.replace(mk_rt(1,-1)*mk_rt(-1,-1), sqrt(m**2-m+sqrt(m-gamma)))
#     pp_.replace(mk_rt(-1,-1)*mk_rt(1,-1), sqrt(m**2-m+sqrt(m-gamma)))
#     pp_.replace(mk_rt(1,1)*mk_rt(1,-1), sqrt(m**2+mk_rt(1)*mk_rt(-1)+m*(mk_rt(1)+mk_rt(-1))))
#     pp_.replace(mk_rt(1,-1)*mk_rt(1,1), sqrt(m**2+mk_rt(1)*mk_rt(-1)+m*(mk_rt(1)+mk_rt(-1))))
#     pp_.replace(mk_rt(1,1)*mk_rt(-1,-1), sqrt(m**2-mk_rt(1)*mk_rt(-1)+m*(mk_rt(1)-mk_rt(-1))))
#     pp_.replace(mk_rt(-1,-1)*mk_rt(1,1), sqrt(m**2-mk_rt(1)*mk_rt(-1)+m*(mk_rt(1)-mk_rt(-1))))
#     return pp_

def reps(pp_):
    pp_ = pp_.replace(a_00*a_01, sqrt(m**2+m*(0+a_0+a_1)+a_0*a_1))
    pp_ = pp_.replace(a_00*a_10, sqrt(m**2+m*(0+a_0-a_0)+a_0*a_0))
    pp_ = pp_.replace(a_00*a_11, sqrt(m**2+m*(0+a_0-a_1)-a_0*a_1))
    pp_ = pp_.replace(a_01*a_10, sqrt(m**2+m*(0+a_1-a_0)-a_1*a_0))
    pp_ = pp_.replace(a_01*a_11, sqrt(m**2+m*(0+a_1-a_1)-a_1*a_1))
    pp_ = pp_.replace(a_10*a_11, sqrt(m**2+m*(0-a_0-a_1)+a_1*a_1))
    return pp_


# In[33]:


reps((co*co).expand())


# In[38]:


(co*co).expand().replace(a_00*a_01, x)

