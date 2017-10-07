from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, x, y, T, S, alpha, beta, gamma
from contextlib import contextmanager
import itertools as it
from numbers import Number

def bigsubs(eqns, x, y):
    return [ eq.subs(x, y) for eq in eqns ]

def nontriv(eqns):
    return [ eq for eq in eqns if eq.free_symbols and eq.expand().free_symbols ]

def only(xs):
    assert len(xs) == 1
    return xs[0]

def show(eqns):
    for i, e in enumerate(eqns):
        print(i, e)
    print()

for subscript in [0, 1, 2, 3, 4]:
    for var in 'abcdefghxy':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)

p_0 = c4*x0**4 + c3*x0**3 + c2*x0**2 + c1*x0 + c0 - y0**2

x0_ = x1 + alpha
y0_ = y1
p_1 = p_0.subs(x0, x0_).subs(y0, y0_).expand().simplify()

x1_ = 1/x2
y1_ = y2/x2**2
p_2 = p_1.subs(x1, x1_).subs(y1, y1_).expand().simplify().as_numer_denom()[0]

wut = p_2.as_poly(x2).as_expr().coeff(x2**4) # square when alpha on p_0
x2_ = x3
y2_ = sqrt(wut)*y3
p_3_ = p_2.subs(x2, x2_).subs(y2, y2_).expand()
p_3 = (p_3_ / p_3_.coeff(x3**4)).expand()

f0_ = p_3.coeff(x3, n=0).subs(y3, 0) # lol
f1_ = p_3.coeff(x3, n=1)
f2_ = p_3.coeff(x3, n=2)
f3_ = p_3.coeff(x3, n=3)

fs = x3**4 + f3*x3**3 + f2*x3**2 + f1*x3 + f0

g_ = x3**2 + g1*x3 + g0
h_ = h1*x3 + h0

eqns = nontriv(equate((g_**2 + h_).expand(), fs, x3))
g1_ = only(solve(eqns[3], g1))
eqns = nontriv(bigsubs(eqns, g1, g1_))
g0_ = only(solve(eqns[2], g0))
eqns = nontriv(bigsubs(eqns, g0, g0_))
h1_ = only(solve(eqns[1], h1))
eqns = nontriv(bigsubs(eqns, h1, h1_))
h0_ = only(solve(eqns[0], h0))
eqns = nontriv(bigsubs(eqns, h0, h0_))

x_ = y3 + g_
y_ = x_*x3

P = 2*y**2 + 2*g1*x*y + 2*g0*x**2 - x**3 + h1*y + h0*x

P_ = P.subs(g0, g0_).subs(g1, g1_).subs(h0, h0_).subs(h1, h1_).subs(f0, f0_).subs(f1, f1_).subs(f2, f2_).subs(f3, f3_)

def go(c0_, c1_, c2_, c3_, c4_, alpha_):
    return P_.subs(c0, c0_).subs(c1, c1_).subs(c2, c2_).subs(c3, c3_).subs(c4, c4_).subs(alpha, alpha_)
# P = f4*x**4 + f3*x**3 + f2*x**2 + f1*x + f0 - y**2
# P0 = P.subs(x, 1/(x - alpha)).subs(y, y/(x - alpha)**2)
# Q = P0.expand().simplify().as_numer_denom()[0].as_poly(x)
# Q
