from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = solve([x - y, y - 3], x)
print(s)
