import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 - 2 * y

def euler(formula, a, b, n, y0):
    
    x, y = sp.symbols('x y')
    formula = sp.sympify(formula)

    function = formula.subs({x: 0, y: 3})

    x0 = a
    h = (b - a) / n
    xes = np.array([x0])
    yes = np.array([y0])
    fun = np.array([])

    while a <= b:
        function = formula.subs({x: x0, y: y0})
        f = sp.sympify(function)
        y1 = y0 + h * f
        a += h
        x1 = a
        xes = np.append(xes, [x0])
        yes = np.append(yes, [y0])
        x0, y0 = x1, y1
        
    return xes, yes