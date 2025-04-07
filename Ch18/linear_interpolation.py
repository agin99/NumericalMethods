import matplotlib.pyplot as plt
import numpy as np

def linear_interp(x0, x1, y0, y1, x): 
    return y0 + (y1 - y0) / (x1 - x0) * (x - x0) 

def quadratic_interp(x0, x1, x2, y0, y1, y2, x):
    prime_func = lambda x0_, x1_, y0_, y1_: (y1_ - y0_) / (x1_ - x0_)
    b0 = y0
    b1 = prime_func(x0, x1, b0, y1)
    b2 = prime_func(x0, x2, b1, prime_func(x1, x2, y1, y2))
    return b0 + b1*(x - x0) + b2*(x - x1)

def compute_newton_coeff(xi, yi):
    prime_func = lambda x0_, x1_, y0_, y1_: (y1_ - y0_) / (x1_ - x0_)
    b = [yi[0]]
    for i in range(len(xi) - 1):
        index = 0
        b0 = []
        for j, k in zip(xi[i+1:], yi[1:]):
            b0.append(prime_func(xi[index], j, yi[index], k))
            index += 1
        yi = b0
        b.append(b0[0])
    return b

def compute_error(order, xi, x, b):
    e = b[order+1]
    for j in xi[:order+1]:
        e *= (x - j)
    return e

def newtons_interp(xi, yi, x, order):
    b = compute_newton_coeff(xi, yi)
    f = b[0]
    for index, i in enumerate(b[1:order + 1]): 
        prod = i
        for j in xi[:index + 1]:
            prod *= (x - j)
        f += prod
    e = None 
    if order + 1 < len(b):
        e = compute_error(order, xi, x, b)    
    return f, e

x = 2
xi = [1, 4, 6, 5]
yi = [0, 1.386294, 1.791759, 1.609438]
order = 3
f, e = newtons_interp(xi, yi, x, order)
print(f"f({x}) = {f} with order {order} err = {e}")