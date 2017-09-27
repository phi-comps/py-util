from util import *
from enuming import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, beta, gamma
from contextlib import contextmanager
import itertools as it
from numbers import Number

@as_list
def sub(eqns, x, y):
    for eq in eqns:
        eq = eq.subs(x, y)
        if eq.free_symbols:
            eq = eq.expand()
            if eq.free_symbols:
                yield Eq(0, eq.rhs - eq.lhs)


eqns = [
    Eq(gamma + m**4 + 2*m**3 + m**2, a**2),
    Eq(4*m**3 + 4*m**2, 2*a*c - b**2),
    Eq(6*m**2 + 2*m, 2*a + 2*b*d + c**2),
    Eq(4*m, 2*c - d**2),
    ]

s = (c, 2*m + d**2 / 2)
eqns = sub(eqns, *s)

s = (a, -b*d - d**4/8 - d**2*m + m**2 + m)
eqns = sub(eqns, *s)

b1, b2 = solve(eqns[1], b)

beta_ = sqrt(2*d**4 + 8*d**2*m + 16*m**2 + 16*m)
b_ = d*(-2*d**2 - 8*m + beta)/4

assert b1.expand() == b_.subs(beta, beta_).expand()
assert b2.expand() == b_.subs(beta, -beta_).expand()

eq = eqns[0]
gamma_ = solve(eq.subs(b, b_), gamma)[0].subs(beta**2, beta_**2).expand()

beta__ = solve(Eq(gamma, gamma_), beta)[0]

num_, den_ = beta__.as_numer_denom()
zero_ = (num_**2 - (den_*beta_)**2).expand()

def int_sqrt(n): # int
    if n < 0:
        return None
    if n < 2:
        return n
    be = sy.perfect_power(n, candidates=[2])
    if be is False:
        return None
    base, exp = be
    assert exp == 2
    return base

betabeta = beta_*beta_

def in_z(m_, d_start, d_end):
    expr = betabeta.subs(m, m_)
    big_expr = gamma_.subs(m, m_)
    for d_ in range(d_start, d_end):
        bb = expr.subs(d, d_)
        assert bb.is_Integer
        bet = int_sqrt(bb)
        if bet is not None:
            yield d_, gamma_.subs(d, d_).subs(beta, bet)


def in_q(m_, d_start, d_end):
    expr = beta_.subs(m, m_)
    big_expr = gamma_.subs(m, m_)
    for d_ in range(d_start, d_end):
        beta__ = expr.subs(d, calkin_wilf(d_))
        # print(beta__)
        if beta__.is_Rational:
            yield d_, big_expr.subs(d, d_).subs(beta, beta__)


def search(m_, d_start, d_end):
    for d_, g_, in in_z(m_, d_start, d_end):
        print('m = {}, d = {}, gamma = {}'.format(m_, d_, g_))

def z_indef(m_, d_start):
    expr = betabeta.subs(m, m_)
    big_expr = gamma_.subs(m, m_)
    for d_ in it.count(d_start):
        bb = expr.subs(d, d_)
        assert bb.is_Integer
        bet = int_sqrt(bb)
        if bet is not None:
            g_ = gamma_.subs(d, d_).subs(beta, bet)
            print('m = {}, d = {}, gamma = {}'.format(m_, d_, g_))