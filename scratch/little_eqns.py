from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, gamma
from contextlib import contextmanager
import itertools as it
from numbers import Number


@contextmanager
def env(name):
    print(r'\begin{' + name + '}')
    yield
    print(r'\end{' + name + '}')

def fmteq(eq):
    return r'{} &= {}'.format(fancy(eq.lhs), fancy(eq.rhs))

def lines(it):
    print((r' \\' + '\n').join(it))

@as_list
def sub(eqns, x, y):
    for eq in eqns:
        eq = eq.subs(x, y)
        if eq.free_symbols:
            eq = eq.expand()
            if eq.free_symbols:
                yield Eq(0, eq.rhs - eq.lhs)

def show(eqns):
    for e in eqns:
        print('{} = {}'.format(e.lhs, e.rhs))

eqns = [
    Eq(gamma + m**4 + 2*m**3 + m**2, a**2),
    Eq(4*m**3 + 4*m**2, 2*a*c - b**2),
    Eq(6*m**2 + 2*m, 2*a + 2*b*d + c**2),
    Eq(4*m, 2*c - d**2),
    ]

show(eqns)

s = (c, 2*m + d**2 / 2)
print()
print('{} = {}'.format(*s))
print()
eqns = sub(eqns, *s)
show(eqns)

s = (a, -b*d - d**4/8 - d**2*m + m**2 + m)
print()
print('{} = {}'.format(*s))
print()
eqns = sub(eqns, *s)
show(eqns)

b1, b2 = solve(eqns[1], b)

print('BRANCH')

s = (b, b1)
print()
print('{} = {}'.format(*s))
print()
eqns1 = sub(eqns, *s)
show(eqns1)
e1 = eqns1[0]

s = (b, b2)
print()
print('{} = {}'.format(*s))
print()
eqns2 = sub(eqns, *s)
show(eqns2)
e2 = eqns2[0]

print()
with env('align'):
    lines((
        fmteq(e1),
        fmteq(e2),
        ))
