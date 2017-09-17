"""
Generators enumerating things (e.g. the rationals).
"""

import itertools
import sympy as sy

def triangle_floor(n):
    """'n's 0-indexed position in the sequence of triangle numbers, rounded down (log n)"""
    if n < 2:
        return n
    lo = 0
    hi = n
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if triangle(mid) == n:
            return mid
        if triangle(mid) < n:
            lo = mid
        else:
            hi = mid
    return lo

def triangle(n):
    """'n'th triangle number"""
    return (n * (n + 1)) // 2

def nn_at_sum(n, target):
    """all 'n'-tuples of non-negative integers whose sum is exactly 'target'"""
    if n == 1:
        yield (target,)
    else:
        for i in range(target):
            for tup in nn_at_sum(n - 1, target - i):
                yield (i,) + tup

def nn(n):
    """all 'n'-tuples of non-negative integers in order of ascending sum"""
    yield (0,)*n
    for i in itertools.count(1):
        yield from nn_at_sum(n, i)

def all_signs(tup):
    """all possible sign combinations of the given tuple"""
    if len(tup) == 0:
        yield ()
    else:
        head = tup[0]
        tail = tup[1:]
        for t in all_signs(tail):
            yield (head,) + t
            if head != 0:
                yield (-head,) + t

def rle(i): # i > 0, sorta.
    """binary run-length encoding of 'i'"""
    run = 0
    digit = 1
    while i:
        if i & 1 == digit:
            run += 1
        else:
            yield run
            run = 1
            digit ^= 1
        i = i >> 1
    yield run

def calkin_wilf(i): # i > 0
    """'i'th rational in a breadth-first traversal of the Calkin-Wilf tree"""
    return sy.continued_fraction_reduce(rle(i))

def all_rat(n):
    """all of \Q^n, roughly ascending in size (bits)"""
    for tup in nn(n):
        rats = tuple(map(calkin_wilf, tup))
        yield from all_signs(rats)
