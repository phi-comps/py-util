
# coding: utf-8

# In[3]:


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


# In[4]:


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


# In[5]:


def mk_rt(*signs):
    acc = sqrt(m-gamma)
    for sign in reversed(signs):
        acc = sqrt(m + sign*acc)
    return acc


# In[26]:


mk_rt(-1, -1, -1)


# In[89]:


coeffs = ((x+a*mk_rt(1,1))*(x+b*mk_rt(1,-1))*(x+c*mk_rt(-1,1))*(x+d*mk_rt(-1,-1))).expand().as_poly(x).coeffs()
for coeff in coeffs:
    display(coeff)
    display('')


# In[23]:


p_ = ((y + a_00)*(y + a*a_01)*(y + b*a_10)*(y + c*a_11)).expand()
coeffs = [ coeff.expand() for coeff in p_.expand().as_poly(y).coeffs() ]
coeffs


# In[15]:


co = coeffs[1]


# In[16]:


co


# In[68]:


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
reps2 = [
    (a_00*a_00, m+a_0),
    (a_01*a_01, m+a_1),
    (a_10*a_10, m-a_0),
    (a_11*a_11, m-a_1),
    (a_00*a_01, sqrt(m**2+m*(0+a_0+a_1)+a_0*a_1)),
    (a_00*a_10, sqrt(m**2+m*(0+a_0-a_0)+a_0*a_0)),
    (a_00*a_11, sqrt(m**2+m*(0+a_0-a_1)-a_0*a_1)),
    (a_01*a_10, sqrt(m**2+m*(0+a_1-a_0)-a_1*a_0)),
    (a_01*a_11, sqrt(m**2+m*(0+a_1-a_1)-a_1*a_1)),
    (a_10*a_11, sqrt(m**2+m*(0-a_0-a_1)+a_1*a_1)),
    ]

reps1 = [
    (a_0*a_0, m+sqrt(m-gamma)),
    (a_1*a_1, m-sqrt(m-gamma)),
    (a_0*a_1, sqrt(m*m-m+gamma)),
    (a_1*a_0, sqrt(m*m-m+gamma)),
    ]

reps11 = [
    (a_0, sqrt(m+sqrt(m-gamma))),
    (a_1, sqrt(m-sqrt(m-gamma))),
    ]

repsp = [
    ((m*(a_0-a_1)).expand(), m*sqrt(2*m-2*sqrt(m*m-m+gamma))),
    ((m*(a_0+a_1)).expand(), m*sqrt(2*m+2*sqrt(m*m-m+gamma))),
    ]

repsc = [
    (a*a, 1),
    (b*b, 1),
    (c*c, 1),
    ]

def reps(pp_):
    pp_ = pp_.expand()
    for old, new in reps2:
        pp_ = (pp_ + pp_.coeff(old)*(new - old)).expand()
    for old, new in reps1 + repsp + reps11 + repsc:
        pp_ = pp_.subs(old, new).expand()
    return pp_


# In[69]:


reps(co*co).subs(((a_0-a_1)).expand(), x)


# In[32]:


pp_ = (co*co).expand()
pp_


# In[36]:


pp_ + pp_.coeff(a_00*a_00)*(x-a_00*a_00)


# In[10]:


aaa = 2*x*y + x + m*y


# In[11]:


aaa.coeff(x*y)


# In[12]:


co


# In[70]:


sqrt(x)

