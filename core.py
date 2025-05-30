import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 - 2 * y

def koshi():
    y0 = float(input())
    a = float(input())
    b = float(input())
    h = float(input())
    d = abs(b - a)
    x0 = a

    result = []

    while a <= b:
        f = f(x0, y0)
        y1 = y0 + h * f
        a += h
        x1 = a
        result.append([round(x0, 1), round(y0, 10), round(f, 3), round(h * f, 3)])
        x0, y0 = x1, y1
    
    for x in result:
        print(x)

    x = list(map(lambda x: x[0], result))
    y = list(map(lambda x: x[1], result))

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'точки Эйлера', color='b')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("График метода Эйлера задачи Коши")
    plt.grid(True)

    plt.show()