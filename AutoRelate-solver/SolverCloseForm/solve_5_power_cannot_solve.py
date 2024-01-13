from sympy.solvers import solve
from sympy import Symbol
# (a+b)**c = d, perturb b and c
# at solve() time, sole use b1/c1 (but not b2/c2, as we want to relate b1/c1 with b2/c2), as well as everything else (a1/a2/d1/d2, otherwise may get empty solution) 

a1 = Symbol('a1')
a2 = Symbol('a2')
b1 = Symbol('b1')
b2 = Symbol('b2')
c1 = Symbol('c1')
c2 = Symbol('c2')
d1 = Symbol('d1')
d2 = Symbol('d2')

# neither solving b1/c1 or b1**c1 works
# though trivial solution, a1=a2, b1=b2, ... should exist
s = solve([(a1 + b1) ** c1 - d1, (a2 + b2) ** c2 - d2, (a1 + b2)** c2 - d1, (a2 + b1) ** c1 - d2], [b1 ** c1, a1, a2, d1, d2])
print(s)
