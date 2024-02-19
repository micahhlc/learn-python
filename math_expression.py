from sympy import symbols, sqrt
from sympy.printing import latex
from IPython.display import display, Math


# Define the variables
a, b, c, x, y, z = symbols('a b c x y z')

# Define the expression
expression = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

# Convert the expression to LaTeX format
latex_expression = latex(expression)

# Print the LaTeX expression

print(latex_expression)

# below need to run in Jupyterlab
from IPython.display import display, Math

# Define the LaTeX expression as a string
# latex_expression = r'\frac{- b - \sqrt{b^{2} - \left(4\right) \; a \; c}}{\left(2\right) \; a}'

# Render the LaTeX expression using display(Math())
# display(Math(latex_expression))