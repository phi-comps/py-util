from sympy import *
from sympy.abc import a, b, c, d, m, x, y, alpha, beta, gamma
from numbers import Number

from util import *
from points import *
from transform import transform
from ec import EllipticCurve, Point

# m_ = -Rational(7, 4)
# cs = [16*m_**2 + 16*m_, 0, 8*m_, 0, 2]
# alpha_ = 1
# coeffs, xtrans, ytrans = transform(*cs, alpha_)
# gx, gy = Rational(53,81), Rational(289,81)
# C = EllipticCurve(*coeffs)
# P0 = Point(gx, gy, 1, C)
# P = P0
# while True:
#     d_ = xtrans.subs(x, P.x).subs(y, P.y)
#     for gamma_ in gammas_at(m_, d_):
#         if check_newly(gamma_, m_):
#             print("gamma:", gamma_)
#             print("m:", m_)
#             print("f(x) =", ((x - gamma_)**2 + gamma_ + m_).expand())
#             print("f^3(x) = p1(x)*p2(x)")
#             p1, p2 = factor(gamma_, m_, d_)
#             print("p1(x) =", p1)
#             print("p2(x) =", p2)
#             print()
#     P = P - P0


m_ = -Rational(7, 4)
cs = [16*m_**2 + 16*m_, 0, 8*m_, 0, 2]
alpha_ = 1
coeffs, xtrans, ytrans = transform(*cs, alpha_)
gx, gy = Rational(53,81), Rational(289,81)
C = EllipticCurve(*coeffs)
P0 = Point(0, 0, 1, C)
P = P0
while True:
    d_ = xtrans.subs(x, P.x).subs(y, P.y)
    for gamma_ in gammas_at(m_, d_):
        if check_newly(gamma_, m_):
            print("gamma:", gamma_)
            print("m:", m_)
            print("f(x) =", ((x - gamma_)**2 + gamma_ + m_).expand())
            print("f^3(x) = p1(x)*p2(x)")
            p1, p2 = factor(gamma_, m_, d_)
            print("p1(x) =", p1)
            print("p2(x) =", p2)
            print()
    P = P - P0
    break