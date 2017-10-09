from sympy import *
from sympy.abc import a, b, c, d, m, x, y, T, S, alpha, beta, gamma

from util import *

__ALL__ = ['transform']

for subscript in range(10):
    for var in 'abcdefghxyST':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)

p0_ = c4*x0**4 + c3*x0**3 + c2*x0**2 + c1*x0 + c0 - y0**2

x0_ = x1 + alpha
y0_ = y1
p1_ = p0_.subs(x0, x0_).subs(y0, y0_)

x1_ = 1/x2
y1_ = y2/x2**2
p2_ = p1_.subs(x1, x1_).subs(y1, y1_).expand().simplify().as_numer_denom()[0]

x2_ = x3
y2_ = sqrt(p2_.coeff(x2**4))*y3
p3_tmp = p2_.subs(x2, x2_).subs(y2, y2_)
p3_ = p3_tmp / p3_tmp.coeff(x3**4)

p3_flat = p3_.expand()
f0_ = p3_flat.coeff(x3, n=0).subs(y3, 0) # lol
f1_ = p3_flat.coeff(x3, n=1)
f2_ = p3_flat.coeff(x3, n=2)
f3_ = p3_flat.coeff(x3, n=3)

p3_nice = x3**4 + f3*x3**3 + f2*x3**2 + f1*x3 + f0

g_ = x3**2 + g1*x3 + g0
h_ = h1*x3 + h0

eqns = nontriv(equate((g_**2 + h_).expand(), p3_nice, x3))
g1_ = only(solve(eqns[3], g1))
eqns = nontriv(bigsubs(eqns, g1, g1_))
g0_ = only(solve(eqns[2], g0))
eqns = nontriv(bigsubs(eqns, g0, g0_))
h1_ = only(solve(eqns[1], h1))
eqns = nontriv(bigsubs(eqns, h1, h1_))
h0_ = only(solve(eqns[0], h0))
eqns = nontriv(bigsubs(eqns, h0, h0_))

# x4 = y3_ + g_
# y4 = T0_*x3_
# yields:
x3_ = y4/x4
y3_ = x4 - g_.subs(x3, x3_)
p4_ = 2*y4**2 + 2*g1*x4*y4 + 2*g0*x4**2 - x4**3 + h1*y4 + h0*x4

# x4_ = 2*x5
# y4_ = 2*y5
# -or-
x4_ = x5/2
y4_ = y5/4
p5_ = p4_.subs(x4, x4_).subs(y4, y4_).expand().simplify()*8

p5__ = p5_.subs(g0, g0_).subs(g1, g1_).subs(h0, h0_).subs(h1, h1_).subs(f0, f0_).subs(f1, f1_).subs(f2, f2_).subs(f3, f3_).subs(x5, x).subs(y5, y)

x0__ = x0_.subs(x1, x1_).subs(x2, x2_).subs(x3, x3_).subs(x4, x4_).subs(y4, y4_).subs(x5, x).subs(y5, y)
y0__ = y0_.subs(y1, y1_).subs(x2, x2_).subs(y2, y2_).subs(x3, x3_).subs(y3, y3_).subs(x4, x4_).subs(y4, y4_).subs(x5, x).subs(y5, y).subs(g0, g0_).subs(g1, g1_).subs(f0, f0_).subs(f1, f1_).subs(f2, f2_).subs(f3, f3_)

canonical = x**3 + a2*x**2 + a4*x + a6 - y**2 - a1*x*y - a3*y

def to_w_coeffs(C):
    a1 = -C.coeff(x*y)
    a2 = C.coeff(x, n=2)
    a3 = -C.subs(x, 0).coeff(y)
    a4 = C.subs(y, 0).coeff(x)
    a6 = C.subs(y, 0).subs(x, 0)
    return a1, a2, a3, a4, a6

def from_w_coeffs(a1_, a2_, a3_, a4_, a6_):
    return canonical.subs(a1, a1_).subs(a2, a2_).subs(a3, a3_).subs(a4, a4_).subs(a6, a6_)

def transform(c0_, c1_, c2_, c3_, c4_, alpha_):
    curve = -p5__.subs(c0, c0_).subs(c1, c1_).subs(c2, c2_).subs(c3, c3_).subs(c4, c4_).subs(alpha, alpha_)
    xtrans = x0__.subs(c0, c0_).subs(c1, c1_).subs(c2, c2_).subs(c3, c3_).subs(c4, c4_).subs(alpha, alpha_)
    ytrans = y0__.subs(c0, c0_).subs(c1, c1_).subs(c2, c2_).subs(c3, c3_).subs(c4, c4_).subs(alpha, alpha_)
    return to_w_coeffs(curve), xtrans, ytrans

def test():
    C, xtrans, ytrans = transform(21, 0, -14, 0, 2, 1)
    x0__ = xtrans.subs(x, Rational(53,81)).subs(y, Rational(289,81))
    y0__ = ytrans.subs(x, Rational(53,81)).subs(y, Rational(289,81))
    assert p0_.subs(c0, 21).subs(c1, 0).subs(c2, -14).subs(c3, 0).subs(c4, 2).subs(x0, x0__).subs(y0, y0__) == 0
