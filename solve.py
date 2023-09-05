from sympy.solvers import solve
from sympy import Symbol
a1 = Symbol('a1')
a2 = Symbol('a2')
b1 = Symbol('b1')
b2 = Symbol('b2')
c1 = Symbol('c1')
c2 = Symbol('c2')
s = solve([a1 + b1 - c1, a2 + b2 - c2, a2 + b1 - c1, a1 + b2 - c2], [a1])
print(s)
