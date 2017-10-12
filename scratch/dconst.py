from sympy import *
from sympy.abc import d, m, x, y, a
from util import *
from enuming import *

for subscript in range(5):
    for var in 'abcdefgh':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)

yy_ = x**2 + 2*(d**2 + 2)*x + 2*d**4

for t in nn(2):
    for p, q in all_signs(t):
        if sqrt(p*p + 2*p*q + 2*q*q).is_Rational:
            # print(p, q)
            c = Rational(p, q)
            p = yy_.subs(x, c*d**2+a).expand()
            foo = p.coeff(d, n=2)
            bar = p.coeff(d, n=0)
            # print(Eq((foo/2)**2, bar))
            sols = solve(Eq((foo/2)**2, bar), d)
            if sols:
                for sol in sols:
                    if sol.is_Rational:
                        print(p, q, sol)

