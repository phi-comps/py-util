from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d
from contextlib import contextmanager
import itertools as it
from numbers import Number

p1_ = mk_deg(4, 1, xg)
p2_ = mk_deg(4, 2, xg)

for subscript in [1, 2]:
    for var in 'abcdp':
        name = '{}{}'.format(var, subscript)
        globals()[name] = sy.Symbol(name)


def bigsubs(eqns, x, y):
    return [ eq.subs(x, y) for eq in eqns ]

def nontriv(eqns):
    return [ eq for eq in eqns if eq.free_symbols ]

@contextmanager
def env(name):
    print(r'\begin{' + name + '}')
    yield
    print(r'\end{' + name + '}')

def fmteq(eq):
    return r'{} &= {}'.format(fancy(eq.lhs), fancy(eq.rhs))

def lines(it):
    print((r' \\' + '\n').join(it))

def fst():
    eqns = nontriv(equate(f_it(3), p1_*p2_, xg))
    with env('align'):
        lines((
            fmteq(Eq(p1, p1_)),
            fmteq(Eq(p2, p2_)),
            ))
    with env('align'):
        lines(map(fmteq, eqns))

def snd():
    pp1 = p1_.subs(d1, d)
    pp2 = p2_.subs(d2, -d)
    eqns = nontriv(equate(f_it(3), pp1*pp2, xg))
    with env('align'):
        lines((
            fmteq(Eq(p1, pp1)),
            fmteq(Eq(p2, pp2)),
            ))
    with env('align'):
        lines(map(fmteq, eqns))

pp1 = p1_.subs(d1, d)
pp2 = p2_.subs(d2, -d)
eqns = nontriv(equate(f_it(3), pp1*pp2, xg))

def show(eqns):
    for i, e in enumerate(eqns):
        print(i, e)
    print()
show(eqns)

def only(xs):
    assert len(xs) == 1
    return xs[0]

c2_ = only(solve(eqns[6], c2))
eqns = nontriv(bigsubs(bigsubs(eqns, c2, c2_), c1, c))
show(eqns)

b2_ = only(solve(eqns[5], b2))
eqns = nontriv(bigsubs(bigsubs(eqns, b2, b2_), b1, b))
show(eqns)

a2_ = only(solve(eqns[4], a2))
eqns1 = nontriv(bigsubs(eqns, a2, a2_))
show(eqns1)

a1_ = only(solve(eqns[4], a1))
eqns2 = nontriv(bigsubs(eqns, a1, a1_))
show(eqns2)