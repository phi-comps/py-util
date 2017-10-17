
# coding: utf-8

# In[1]:

import sympy as sy
from sympy import Symbol, Eq, Rational, sqrt, solve
from sympy.abc import a, b, c, d, m, x, y, G, H, T, S, alpha, beta, gamma
sy.init_printing()

from IPython.display import display, Latex

from util import *

__ALL__ = [
    'suber',
    'a1_', 'a2_', 'a3_', 'a4_', 'a6_',
    'c0', 'c1', 'c2', 'c3', 'c4', 'alpha'
    'x0__',
    'y0__',
    'p0__',
    ]


# In[2]:

for subscript in range(10):
    for var in 'abcdefghxyST':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)

def show(i):
    ltx = [
        r'\begin{align}',
        r'x_{} &\mapsto {} \\'.format(i, sy.latex(globals()['x{}_'.format(i)])),
        r'y_{} &\mapsto {} \\'.format(i, sy.latex(globals()['y{}_'.format(i)])),
        r'0 &= ' + sy.latex(globals()['p{}_'.format(i + 1)]),
        r'\end{align}',   
    ]
    display(Latex('\n'.join(ltx)))


# In[3]:

canonical = x**3 + a2*x**2 + a4*x + a6 - y**2 - a1*x*y - a3*y
Eq(0, canonical)


# In[4]:

p0_ = c4*x0**4 + c3*x0**3 + c2*x0**2 + c1*x0 + c0 - y0**2
Eq(0, p0_)


# In[5]:

x0_ = x1 + alpha
y0_ = y1
p1_ = p0_.subs(x0, x0_).subs(y0, y0_)
show(0)


# In[6]:

x1_ = 1/x2
y1_ = y2/x2**2
p2_ = p1_.subs(x1, x1_).subs(y1, y1_).expand().simplify().as_numer_denom()[0]
show(1)


# In[7]:

x2_ = x3
y2_ = sqrt(p2_.coeff(x2**4))*y3
p3_tmp = p2_.subs(x2, x2_).subs(y2, y2_)
p3_ = (p3_tmp / p3_tmp.coeff(x3**4)).expand().as_poly(x3, y3).as_expr()
show(2)


# In[8]:

f0_ = p3_.coeff(x3, n=0).subs(y3, 0) # lol
f1_ = p3_.coeff(x3, n=1)
f2_ = p3_.coeff(x3, n=2)
f3_ = p3_.coeff(x3, n=3)

display(
    Eq(f0, f0_),
    Eq(f1, f1_),
    Eq(f2, f2_),
    Eq(f3, f3_),
    )

x_with_fs = x3**4 + f3*x3**3 + f2*x3**2 + f1*x3 + f0

display(Eq(y3**2, x_with_fs))


# In[9]:

G_ = x3**2 + g1*x3 + g0
H_ = h1*x3 + h0

display(
    Eq(G, G_),
    Eq(H, H_),
    Eq(G**2 + H, x_with_fs),
    Eq(G_**2 + H_, x_with_fs),
    )


# In[10]:

eqns = nontriv(equate((G_**2 + H_).expand(), x_with_fs, x3))
g1_ = only(solve(eqns[3], g1))
eqns = nontriv(bigsubs(eqns, g1, g1_))
g0_ = only(solve(eqns[2], g0))
eqns = nontriv(bigsubs(eqns, g0, g0_))
h1_ = only(solve(eqns[1], h1))
eqns = nontriv(bigsubs(eqns, h1, h1_))
h0_ = only(solve(eqns[0], h0))
eqns = nontriv(bigsubs(eqns, h0, h0_))

display(
    Eq(g0, g0_),
    Eq(g1, g1_),
    Eq(h0, h0_),
    Eq(h1, h1_),
    )


# In[11]:

# x4 = y3_ + g_
# y4 = T0_*x3_
# yields:
x3_ = y4/x4
y3_ = x4 - G_.subs(x3, x3_)
p4_ = 2*y4**2 + 2*g1*x4*y4 + 2*g0*x4**2 - x4**3 + h1*y4 + h0*x4
show(3)


# In[12]:

# x4_ = 2*x5
# y4_ = 2*y5
# -or-
x4_ = x5/2
y4_ = y5/4
p5_ = p4_.subs(x4, x4_).subs(y4, y4_).expand().simplify()*8
show(4)


# Yay!

# In[13]:

x0__ = x0_.subs(x1, x1_).subs(x2, x2_).subs(x3, x3_).subs(x4, x4_).subs(y4, y4_).subs(x5, x).subs(y5, y)
y0__ = y0_.subs(y1, y1_).subs(x2, x2_).subs(y2, y2_).subs(x3, x3_).subs(y3, y3_).subs(x4, x4_).subs(y4, y4_).subs(x5, x).subs(y5, y).subs(g0, g0_).subs(g1, g1_).subs(f0, f0_).subs(f1, f1_).subs(f2, f2_).subs(f3, f3_)
p0__ = p5_.subs(g0, g0_).subs(g1, g1_).subs(h0, h0_).subs(h1, h1_).subs(f0, f0_).subs(f1, f1_).subs(f2, f2_).subs(f3, f3_).subs(x5, x).subs(y5, y)


# In[14]:

display(Eq)


# In[15]:

display(Latex('\n'.join([
        r'\begin{align}',
        r'x_0 &\mapsto {} \\'.format(sy.latex(x0__)),
        r'y_0 &\mapsto {} \\'.format(sy.latex(y0__)),
        r'0 &= ' + sy.latex(p0__),
        r'\end{align}',   
    ])))


# In[16]:

def to_w_coeffs(C):
    a1 = -C.coeff(x*y)
    a2 = C.coeff(x, n=2)
    a3 = -C.subs(x, 0).coeff(y)
    a4 = C.subs(y, 0).coeff(x)
    a6 = C.subs(y, 0).subs(x, 0)
    return a1, a2, a3, a4, a6

def from_w_coeffs(a1_, a2_, a3_, a4_, a6_):
    return canonical.subs(a1, a1_).subs(a2, a2_).subs(a3, a3_).subs(a4, a4_).subs(a6, a6_)


# In[17]:

a1_, a2_, a3_, a4_, a6_ = to_w_coeffs(p0__)
display(
    Eq(a1, a1_),
    Eq(a2, a2_),
    Eq(a3, a3_),
    Eq(a4, a4_),
    Eq(a6, a6_),
    )


# In[18]:

def suber(c0_, c1_, c2_, c3_, c4_, alpha_):
    return lambda expr_: expr_.subs(c0, c0_).subs(c1, c1_).subs(c2, c2_).subs(c3, c3_).subs(c4, c4_).subs(alpha, alpha_)

def transform(*args):
    sub = suber(*args)
    curve = sub(p0__)
    xtrans = sub(x0__)
    ytrans = sub(y0__)
    return to_w_coeffs(curve), xtrans, ytrans


# In[19]:

sub = suber(21, 0, -14, 0, 2, 1)

display(Latex('\n'.join([
        r'\begin{align}',
        r'x_0 &\mapsto {} \\'.format(sy.latex(sub(x0__))),
        r'y_0 &\mapsto {} \\'.format(sy.latex(sub(y0__))),
        r'0 &= ' + sy.latex(sub(p__)),
        r'\end{align}',   
    ])))

display(
    Eq(a1, sub(a1_)),
    Eq(a2, sub(a2_)),
    Eq(a3, sub(a3_)),
    Eq(a4, sub(a4_)),
    Eq(a6, sub(a6_)),
    )


# In[ ]:

def test():
    C, xtrans, ytrans = transform(21, 0, -14, 0, 2, 1)
    xt = xtrans.subs(x, Rational(53,81)).subs(y, Rational(289,81))
    yt = ytrans.subs(x, Rational(53,81)).subs(y, Rational(289,81))
    assert p0_.subs(c0, 21).subs(c1, 0).subs(c2, -14).subs(c3, 0).subs(c4, 2).subs(x0, xt).subs(y0, yt) == 0
test()

