from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma
from contextlib import contextmanager
import itertools as it
from numbers import Number

from transform import transform
from ec import EllipticCurve

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

    eqns = nontriv(bigsubs(bigsubs(eqns, d1, d), d2, -d))
    eqns = nontriv(bigsubs(bigsubs(eqns, a1, a), a2, a))
    eqns = nontriv(bigsubs(bigsubs(eqns, b1, b), b2, -b))
    eqns = nontriv(bigsubs(bigsubs(eqns, c1, c), c2, c))

    eqns = nontriv(bigsubs(eqns, c, only(solve(eqns[3], c))))
    eqns = nontriv(bigsubs(eqns, a, only(solve(eqns[2], a))))

    gammas = [ only(solve(eqns[0].subs(b, b_), gamma)) for b_ in solve(eqns[1], b) ]

    def gammas_at(d_, m_):
        for gamma_ in gammas:
            yield gamma_.subs(d, d_).subs(m, m_)

    return gammas_at

gammas_at = mk_gammas_at()

def test1():
    gammas = list(gammas_at(1, -Rational(7,4)))
    for g in [Rational(11,16), Rational(1,2)]:
        assert g in gammas


qq = 2*d**4 + 8*d**2*m + 16*m**2 + 16*m

class Points(object):

    def __init__(self, m_, alpha_):
        self.m = m_
        self.ec, selt.xtrans, self.ytrans = tranform(16*m_**2 + 16*m_, 0, 8*m_, 0, 2, alpha_)
        self.eco = EllipticCurve(self.ec)
        self.gens = _

    def gammas():
        for gx, gy in self.gens:
            yield from gammas_at(xtrans.subs(x, gx).subs(y, gy), self.m)