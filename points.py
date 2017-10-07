from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma
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
    for var in 'abcdefgh':
        name = '{}{}'.format(var, subscript)
        globals()[name] = sy.Symbol(name)


def mk_gammas_at():

    p1_ = mk_deg(4, 1, xg)
    p2_ = mk_deg(4, 2, xg)
    eqns = nontriv(equate(f_it(3), p1_*p2_, xg))
    show(eqns)

    eqns = nontriv(bigsubs(bigsubs(eqns, d1, d), d2, -d))
    eqns = nontriv(bigsubs(bigsubs(eqns, a1, a), a2, a))
    eqns = nontriv(bigsubs(bigsubs(eqns, b1, b), b2, -b))
    eqns = nontriv(bigsubs(bigsubs(eqns, c1, c), c2, c))

    eqns = nontriv(bigsubs(eqns, c, only(solve(eqns[3], c))))
    eqns = nontriv(bigsubs(eqns, a, only(solve(eqns[2], a))))

    gammas = [ eqns[0].subs(b, b_) for b_ in solve(eqns[1], b) ]

    def gammas_at(d_, m_):
        for gamma_ in gammas:
            yield gamma_.subs(d, d_).subs(m, m_)

    return gammas_at


qq = 2*d**4 + 8*d**2*m + 16*m**2 + 16*m

def qq_of(m_):
    return qq.subs(m, m_)

def ec_of(m_, alpha_):
    qq.subs
    return x_trans, y_trans, coeffs

g_ = x**2 + g1*x + g0
h_ = h1*x + h0

# pp1 = p1_.subs(d1, d)
# pp2 = p2_.subs(d2, -d)
# eqns = nontriv(equate(f_it(3), pp1*pp2, xg))