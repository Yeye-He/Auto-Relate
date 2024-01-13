from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
s = solve(x**2 - 1, x)
print(s)
