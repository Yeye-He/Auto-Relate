from sympy.solvers import solve
from sympy import Symbol
# a + b = c, perburb a (swap a1 and a2)

a1 = Symbol('a1')
a2 = Symbol('a2')
b1 = Symbol('b1')
b2 = Symbol('b2')
c1 = Symbol('c1')
c2 = Symbol('c2')

eqns_1 = [a1 + b1 - c1, a2 + b2 - c2, a2 + b1 - c1, a1 + b2  - c2]

s = solve(eqns_1, [a1,  b2, b1, c1, c2], dict=True)
print(s)

# change order
s = solve(eqns_1, [b2, b1, c1, c2, a1], dict=True)
print(s)


print('below: change the order of variables to solve, and answer changed')
# add a2 (this is solving a1/a2/b2, seemingly based on the order in which they appear)
s = solve(eqns_1, [a1, a2, b2, b1, c1, c2], dict=True)
print(s)

# add a2, change order (why is this solving a1/b1/b2?)
s = solve(eqns_1, [b2, b1, c1, c2, a1, a2], dict=True)
print(s)




# change eqns order
eqns_2 = [a2 + b1 - c1, a1 + b2 - c2, a1 + b1 - c1, a2 + b2 - c2]


print('change the order of equations (do not seem to matter, when compared to above)')

s = solve(eqns_2, [a1,  b2, b1, c1, c2], dict=True)
print(s)

s = solve(eqns_2, [b2, b1, c1, c2, a1], dict=True)
print(s)

s = solve(eqns_2, [a1, a2, b2, b1, c1, c2], dict=True)
print(s)

s = solve(eqns_2, [b2, b1, c1, c2, a1, a2], dict=True)
print(s)


# solve a1-a2, why we get [], and not 0??
print('solve a1-a2, why we get [], and not 0??')
s = solve(eqns_2, [a1, a2, a2-a1], dict=True, implicit=True)
print(s)


print('solve a1-a2, cannot eval a1-a2, no results returned for a1-a2??')
s = solve(eqns_2, [a1-a2, a1,  b2, b1, c1, c2], dict=True, implicit=True)
print(s)
