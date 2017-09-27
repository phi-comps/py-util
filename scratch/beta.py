from sympy import *
from sympy.abc import *

gamma_phi = Rational(1, 2)
m_phi = -Rational(7, 4)

s = 2*x**4 + 8*m*x**2 + 16*m**2 + 16*m

s_phi = s.subs(m, m_phi)
