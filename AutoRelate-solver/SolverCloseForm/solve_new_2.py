from sympy import solve 
from sympy import Symbol, symbols

a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = symbols('a1, a2, b1, b2, c1, c2, d1, d2, e1, e2')

# formula: (a + b) * c == d
# perturb b/C
eqns = [(a1 + b1) * c1 - d1, (a2 + b2) * c2 - d2, (a1 + b2) * c2 - d1, (a2 + b1) * c1 - d2]

s = solve(eqns, [a1, a2, b1, c1, d1, d2], dict=True)
print(s)


#s = solve(eqns, [a1, d1, b1, c1, b2, c2], dict=True)
#print(s)

