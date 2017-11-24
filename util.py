"""
Miscellaneous polynomial-related utility objects.
"""

import string
import sympy as sy
from sympy.abc import m, x, gamma

xg = sy.Symbol('xg')

quad_split = (x - gamma)**2 + gamma + m
quad_joined = xg**2 + gamma + m

def f_it(n):
    assert n > 0
    f = x
    while n > 1:
        f = f.subs(x, quad_split)
        n -= 1
    return f.subs(x, quad_joined).expand()

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


def only(xs):
    assert len(xs) == 1
    return xs[0]

def bigsubs(eqns, x, y):
    return [ eq.subs(x, y) for eq in eqns ]

def nontriv(eqns):
    return [ eq for eq in eqns if eq.free_symbols and eq.expand().free_symbols ]


# def fancy(expr):
#     return sy.latex(expr).replace('xg', r'\xg')

# def show(eqns):
#     for i, e in enumerate(eqns):
#         print(i, e)
#     print()