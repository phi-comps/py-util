from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, beta, gamma
from contextlib import contextmanager
import itertools as it
from numbers import Number


@contextmanager
def env(name):
    print(r'\begin{' + name + '}')
    yield
    print(r'\end{' + name + '}')

def fmteqt(eq):
    return r'{} &= {}'.format(fancy(eq.lhs), fancy(eq.rhs))

def fmteq(eq):
    return r'{} = {}'.format(fancy(eq.lhs), fancy(eq.rhs))

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

print(fmteq(Eq(gamma, gamma_)))
print()
print(fmteq(Eq(beta, beta_)))
print()
print(fmteq(Eq(beta, -beta_)))

print()
print()

beta__ = solve(Eq(gamma, gamma_), beta)[0]

print(fmteq(Eq(beta, beta__)))

# zero_ = (beta_**2 - beta__**2).expand()
n_, d_ = beta__.as_numer_denom()
zero_ = (n_**2 - (d_*beta_)**2).expand()

print()
print(fmteq(Eq(0, zero_)))

print()

print(r'''\[
\begin{array}{|c|l|}
\hline
\mbox{exponent of }d & \mbox{coefficient of }d\\
\hline''')

for i in range(0, zero_.as_poly(d).degree() + 1):
    print(r'{} & {} \\'.format(i, fancy(zero_.coeff(d, n=i))))

print(r'''\hline
\end{array}
\]
''')

print(fmteq(Eq(gamma, gamma_.as_poly(beta).as_expr())))
# s = (b, b1)
# eqns1 = sub(eqns, *s)
# e1 = eqns1[0]

# s = (b, b2)
# eqns2 = sub(eqns, *s)
# e2 = eqns2[0]
