import numpy as np
import sympy as sp

def euler(formula, a, b, n, y0):
    
    x, y = sp.symbols('x y')
    formula = sp.sympify(formula)

    function = formula.subs({x: 0, y: 3})

    x0 = a
    h = (b - a) / n
    xes = np.array([x0])
    yes = np.array([y0])

    while a <= b:
        function = formula.subs({x: x0, y: y0})
        f = sp.sympify(function)
        a += h
        x0, y0 = a, y0 + h * f
        xes = np.append(xes, [x0])
        yes = np.append(yes, [y0])

    return xes, yes

def hoyne(formula, a, b, n, y0):
    x, y = sp.symbols('x y')
    formula = sp.sympify(formula)

    function = formula.subs({x: 0, y: 3})

    x0 = a
    h = (b - a) / n
    xes = np.array([x0])
    yes = np.array([y0])

    while a <= b:
        function = formula.subs({x: x0, y: y0})
        k = sp.sympify(function)
        function = formula.subs({x: x0 + (h / 2), y: y0 + (h / 2) * k})
        a += h
        x0, y0 = a, y0 + h * sp.sympify(function)
        xes = np.append(xes, [x0])
        yes = np.append(yes, [y0])

    return xes, yes