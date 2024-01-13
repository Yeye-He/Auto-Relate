from sympy import symbols, Eq, solve

##asked chatgpt for how to solve x using only a fixed set of variables, got this answer

# Define the variables
a, b, x, c, y, d, e = symbols('a b x c y d e')

# Given equations
equation1 = Eq(a*x + b*y, c)
equation2 = Eq(y, d*a + e*c)

# Substitute y from equation2 into equation1
substituted_equation = equation1.subs(y, solve(equation2, y)[0])

# Now, solve for x in terms of a and c
solution = solve(substituted_equation, x)

print(solution)


