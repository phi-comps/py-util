from util import *

def split(n):
    p1 = mk_deg(n, 1, xg)
    p2 = mk_deg(8 - n, 2, xg)
    print(r'\begin{align}')
    print('p_1 &=', fancy(p1), r'\\')
    print('p_2 &=', fancy(p2))
    print(r'\end{align}')
    print(r'\begin{align}')
    for l, r in equate(f_it(3), p1*p2, xg):
        print(fancy(l), '&=', fancy(r), r'\\')
    print(r'\end{align}')

# print all of the candidate equations
for n in [2, 3, 4]:
    split(n)
    print()
