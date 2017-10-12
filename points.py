from sympy import *
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma
from numbers import Number

from util import *
from transform import transform
from ec import EllipticCurve, Point


for subscript in range(5):
    for var in 'abcdefgh':
        name = '{}{}'.format(var, subscript)
        globals()[name] = Symbol(name)


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

def gammas_at(m_, d_):
    for gamma_ in gammas:
        yield gamma_.subs(d, d_).subs(m, m_)


def test1():
    gammas = list(gammas_at(-Rational(7,4), 1))
    for g in [Rational(11,16), Rational(1,2)]:
        assert g in gammas
test1()

qq = 2*d**4 + 8*d**2*m + 16*m**2 + 16*m

class Points(object):

    def __init__(self, m_, alpha_):
        self.m = m_
        self.coeffs, selt.xtrans, self.ytrans = tranform(16*m_**2 + 16*m_, 0, 8*m_, 0, 2, alpha_)
        self.C = EllipticCurve(self.coeffs)
        self.gens = 1/0

    def gammas():
        for gx, gy in self.gens:
            yield from gammas_at(self.m, xtrans.subs(x, gx).subs(y, gy))


# def abc(gamma_, m_, d_):
#     c_ = (4*m_ + d_**2)/2
#     a_ = -sqrt(gamma_ + m_**4 + 2*m_**3 + m_**2 + m_) # to align with sympy's fact alg
#     b_ = (6*m_**2 + 2*m_ - 2*a_ - c_**2)/(-2*d_)
#     return a_, b_, c_

xg_ = x - gamma
p1_ = a + b*xg_ + c*xg_**2 + d*xg_**3 + xg_**4
p2_ = a - b*xg_ + c*xg_**2 - d*xg_**3 + xg_**4

def factor(gamma_, m_, d_):
    f_ = ((x - gamma_)**2 + gamma_ + m_).expand().as_poly(x)
    fff_ = f_.compose(f_).compose(f_).as_expr().expand()
    c_ = (4*m_ + d_**2)/2
    a_ = sqrt(gamma_ + m_**4 + 2*m_**3 + m_**2 + m_)
    b_ = (6*m_**2 + 2*m_ - 2*a - c_**2)/(-2*d_)
    fff = p1_*p2_
    if fff_ == fff.subs(d, d_).subs(c, c_).subs(b, b_).subs(a, a_).subs(gamma, gamma_).expand():
        return (
            p1_.subs(d, d_).subs(c, c_).subs(b, b_).subs(a, a_).subs(gamma, gamma_).expand(),
            p2_.subs(d, d_).subs(c, c_).subs(b, b_).subs(a, a_).subs(gamma, gamma_).expand(),
            )
    if fff_ == fff.subs(d, d_).subs(c, c_).subs(b, b_).subs(a, -a_).subs(gamma, gamma_).expand():
        return (
            p1_.subs(d, d_).subs(c, c_).subs(b, b_).subs(a, -a_).subs(gamma, gamma_).expand(),
            p2_.subs(d, d_).subs(c, c_).subs(b, b_).subs(a, -a_).subs(gamma, gamma_).expand(),
            )
    assert False

def check_newly(gamma_, m_):
    return not sqrt(-gamma_ - m_).is_Rational and (not sqrt(-2*m_ + 2*sqrt(gamma_ + m_**2 + m_)).is_Rational and not sqrt(-2*m_ - 2*sqrt(gamma_ + m_**2 + m_)).is_Rational)
