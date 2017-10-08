from util import *
from sympy import *
import sympy as sy
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma
from contextlib import contextmanager
import itertools as it
from numbers import Number

from transform import transform
from ec import EllipticCurve, Point

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


p1_ = mk_deg(4, 1, xg)
p2_ = mk_deg(4, 2, xg)
eqns = nontriv(equate(f_it(3), p1_*p2_, xg))

eqns = nontriv(bigsubs(bigsubs(eqns, d1, d), d2, -d))
eqns = nontriv(bigsubs(bigsubs(eqns, a1, a), a2, a))
eqns = nontriv(bigsubs(bigsubs(eqns, b1, b), b2, -b))
eqns = nontriv(bigsubs(bigsubs(eqns, c1, c), c2, c))
eqns1 = eqns

eqns = nontriv(bigsubs(eqns, c, only(solve(eqns[3], c))))
eqns = nontriv(bigsubs(eqns, a, only(solve(eqns[2], a))))

gammas = [ only(solve(eqns[0].subs(b, b_), gamma)) for b_ in solve(eqns[1], b) ]

def gammas_at(d_, m_):
    for gamma_ in gammas:
        yield gamma_.subs(d, d_).subs(m, m_)

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
        # self.gens = 

    def gammas():
        for gx, gy in self.gens:
            yield from gammas_at(xtrans.subs(x, gx).subs(y, gy), self.m)

def abc(gamma_, m_, d_):
    c_ = (4*m_ + d_**2)/2
    a_ = sqrt(gamma_ + m_**4 + 2*m_**3 + m_**2 + m_) # to align with sympy's fact alg
    b_ = (6*m_**2 + 2*m_ - 2*a_ - c_**2)/(-2*d_)
    return a_, b_, c_

def factors(a_, b_, c_, d_):
    xg_ = x - gamma
    p1 = a_ + b_*xg_ + c_*xg_**2 + d_*xg_**3 + xg_**4
    p2 = a_ - b_*xg_ + c_*xg_**2 - d_*xg_**3 + xg_**4
    return p1, p2

def check_newly(gamma_, m_):
    return not sqrt(-gamma_ - m_).is_Rational and (not sqrt(-2*m_ + 2*sqrt(gamma_ + m_**2 + m_)).is_Rational and not sqrt(-2*m_ - 2*sqrt(gamma_ + m_**2 + m_)).is_Rational)


# def lame():
m_ = -Rational(7, 4)
cs = [16*m_**2 + 16*m_, 0, 8*m_, 0, 2]
alpha_ = 1
coeffs, xtrans, ytrans = transform(*cs, alpha_)
# print(coeffs)
gx, gy = Rational(53,81), Rational(289,81)
C = EllipticCurve(*coeffs)
P0 = Point(gx, gy, 1, C)
P = P0
for _ in range(10):
    d_ = xtrans.subs(x, P.x).subs(y, P.y)
    for g_ in gammas_at(d_, m_):
        if check_newly(g_, m_):
            print("gamma:", g_)
            print("m:", m_)
            print("f(x) =", ((x - g_)**2 + g_ + m_).expand())
            print("f^3(x) = p_1(x)*p_2(x)")
            a_, b_, c_ = abc(g_, m_, d_)
            p1, p2 = factors(a_, b_, c_, d_)
            f3 = f_it(3).subs(xg, x - gamma).subs(gamma, g_).subs(m, m_).expand()
            print()
            print("p_1(x) = ", p1.subs(gamma, g_).expand())
            print()
            print("p_2(x) = ", p2.subs(gamma, g_).expand())
            print()
            fs = f3.factor()
            n, _ = fs.as_numer_denom()
            l, r = n.as_two_terms()
            p1_ = (l/l.coeff(x**4)).expand()
            p2_ = (r/r.coeff(x**4)).expand()
            # p1_ = l/l.
            print("p_1_(x) = ", p1_)
            print()
            print("p_2_(x) = ", p2_)
            print()
            print()
            if (p1*p2).subs(gamma, g_).expand() != f3:
                print("BAD")
                print((p1*p2).subs(gamma, g_).expand())
                print()
                print(f3)
                assert False
            assert (p1*p2).subs(gamma, g_).expand() == f3
            print()
            print()
    P = P + P0
