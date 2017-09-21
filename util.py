"""
Miscellaneous polynomial-related utility objects.
"""

import string
import sympy as sy

g, m = sy.symbols('gamma m')
x, xg = sy.symbols('x xg')

quad = (x - g)**2 + g + m
quad_ = xg**2 + g + m

def f_it(n):
    assert n > 0
    f = x
    while n > 1:
        f = f.subs(x, quad)
        n -= 1
    return f.subs(x, quad_).expand()

def as_list(f):
    def g(*args, **kwargs):
        return list(f(*args, **kwargs))
    return g

@as_list
def equate(p1, p2, var):
    p1_ = p1.expand()
    p2_ = p2.expand()
    mdeg = max(p1_.as_poly(var).degree(), p2_.as_poly(var).degree())
    for deg in range(mdeg + 1):
        yield sy.Eq(p1_.coeff(var, n=deg), p2_.coeff(var, n=deg))

def mk_deg(n, sub, var):
    assert n > 0
    cs = iter(sy.symbols(' '.join('{}{}'.format(c, sub) for c in string.ascii_lowercase)))
    p = 0
    for i in range(n):
        p += next(cs)*var**i
    return p + var**n

def fancy(expr):
    return sy.latex(expr).replace('xg', r'\xg')
