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

def besteuler(formula, a, b, n, y0):
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

        function = formula.subs({x: x0 + h / 2, y: y0 + ((h / 2) * f) })
        dy = h * sp.sympify(function)
        a += h
        x0, y0 = a, y0 + dy
        xes = np.append(xes, [x0])
        yes = np.append(yes, [y0])

    return xes, yes

def kyt(formula, a, b, n, y0):
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
        k1 = h * f

        function = formula.subs({x: x0 + h / 2, y: y0 + k1 / 2})
        k2 = h * sp.sympify(function)

        function = formula.subs({x: x0 + h / 2, y: y0 + k2 / 2})
        k3 = h * sp.sympify(function)

        function = formula.subs({x: x0 + h, y: y0 + k3})
        k4 = h * sp.sympify(function)

        a += h
        x0, y0 = a, y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        xes = np.append(xes, [x0])
        yes = np.append(yes, [y0])

    return xes, yes

def adams(formula, a, b, n, y0):
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
        y1 = y0 + h * f
        x1 = a + h

        function = formula.subs({x: x1, y: y1})
        y1 = y0 + (h / 2) * (f + sp.simplify(function))

        a = x1
        x0, y0 = x1, y1
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