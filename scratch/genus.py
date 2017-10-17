from points import *

beta_ = sqrt(2)*sqrt(d**4 + 4*d**2*m + 8*m**2 + 8*m)
gamma_ = gammas[0].subs(beta_, beta).expand()
a1_, a0_ = gamma_.coeff(beta, n=1), gamma_.coeff(beta, n=0)
P_ = (((beta*a1_ + a0_)*(beta*a1_ - a0_)).expand() + a0_*gamma)**2-(beta*a1_*gamma)**2
P__ = P_.expand().subs(beta, beta_).expand()