#https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html
from sympy.solvers import solve
from sympy import *
x = Symbol('x')
y = Symbol('y')
s = solve([x*y, x*y - x], [x, y])
print(s)

a, b, c, d = symbols('a, b, c, d')#, real=True)
system = [a**2 + a*c, a - b]
s = nonlinsolve(system, [a, b])
print(s)

