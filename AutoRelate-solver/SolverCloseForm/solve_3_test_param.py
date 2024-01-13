from sympy.solvers import solve
from sympy import Symbol
# (a + b) = c, perturb a and b

a1 = Symbol('a1')
a2 = Symbol('a2')
b1 = Symbol('b1')
b2 = Symbol('b2')
c1 = Symbol('c1')
c2 = Symbol('c2')

# solving [a1, b1, c1, c2] does not directly produce desired results, because the gt is relating to "a1 + b1" and not a1/b1 separately
#s = solve([(a1 + b1) - c1, (a2 + b2) - c2, (a2 + b2) - c1, (a1 + b1) - c2], [a1, b1, c1, c2])


# can solve a1+b1 as a symbol, per https://docs.sympy.org/latest/modules/solvers/solvers.html#sympy.solvers.solvers.solve: "When an object other than a Symbol is given as a symbol, it is isolated algebraically and an implicit solution may be obtained. This is mostly provided as a convenience to save you from replacing the object with a Symbol and solving for that Symbol."
s = solve([(a1 + b1) - c1, (a2 + b2) - c2, (a2 + b2) - c1, (a1 + b1) - c2], [a1+b1, c1, c2], simplify=True)
print(s)

#s = solve([(a1 + b1) - c1, (a2 + b2) - c2, (a2 + b2) - c1, (a1 + b1) - c2], [a1+b1, a2+b2, c1, c2])
#print(s)
