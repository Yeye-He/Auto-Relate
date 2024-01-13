from sympy.solvers import solve
from sympy import Symbol
# (a+b)*c = d, perturb b and c
# at solve() time, sole use b1/c1 (but not b2/c2, as we want to relate b1/c1 with b2/c2), as well as everything else (a1/a2/d1/d2) 

a1 = Symbol('a1')
a2 = Symbol('a2')
b1 = Symbol('b1')
b2 = Symbol('b2')
c1 = Symbol('c1')
c2 = Symbol('c2')
d1 = Symbol('d1')
d2 = Symbol('d2')

eqns = [(a1 + b1) * c1 - d1, (a2 + b2) * c2 - d2, (a1 + b2)* c2 - d1, (a2 + b1) * c1 - d2]

# solve only b1/c1?
s = solve(eqns, [b1, c1], dict=True)
print(s)

# solve only b1/c1/b2/c2?
s = solve(eqns, [b1, c1, b2, c2], dict=True, manual=True)
print(s)

# solve b1-b2, c1-c2? (no result, because if c/d are 0, b1 may not need to be the same as b2?? not sure)
s = solve(eqns, [b1-b2, c1-c2], dict=True)
print(s)


# leave out b2/c2
s = solve(eqns, [b1, c1, a1, a2, d1, d2], dict=True)
print(s)

# leave out b2/c2, change order of solve var, does not seem to have an effect (b1/c1 is still solved)
s = solve(eqns, [a1, a2, d1, d2, b1, c1], dict=True)
print(s)

# leave in b2/c2 to solve (same result as above, one more special =0 solution)
s = solve(eqns, [b1, c1, b2, c2, a1, a2, d1, d2], dict=True)
print(s)

# leave in b2/c2 to solve, change var order (same as result as above, one more special =0 solution)
s = solve(eqns, [a1, a2, d1, d2, b1, c1, b2, c2], dict=True)
print(s)

s = solve(eqns, [b1, c1, b2, c2, a1, a2, d1, d2], dict=True)
print(s)
