import math
import numpy as np
import matplotlib.pyplot as plt

def f(poly_form, x):
    poly_output = 0
    for index, i in enumerate(poly_form): 
        poly_output += i*np.pow(x, index)
    return poly_output

def bisection(poly, x_u, x_l, e_s): 
    prev_x_r = 0
    e_a = 0
    while True:
        x_r = (x_u + x_l) / 2
        if f(poly, x_r)*f(poly, x_l) < 0:
            x_u = x_r
        elif f(poly, x_r)*f(poly, x_l) > 0: 
            x_l = x_r
        e_a = abs((x_r - prev_x_r) / x_r)
        if e_a < e_s:
            return x_r, e_a
        prev_x_r = x_r

def false_position(poly, x_u, x_l, e_s): 
    prev_x_r = 0
    e_a = 0
    while True:
        x_r = x_u - f(poly, x_u)*(x_l - x_u) / (f(poly, x_l) - f(poly, x_u))
        if f(poly, x_r)*f(poly, x_l) < 0:
            x_u = x_r
        elif f(poly, x_r)*f(poly, x_l) > 0: 
            x_l = x_r
        e_a = abs((x_r - prev_x_r) / x_r)
        if e_a < e_s:
            return x_r, e_a
        prev_x_r = x_r

print("(5.1)")
polynomial = [5.5, 2.4, -0.6]
print(bisection(polynomial, 10, 5, 0.1))
print(false_position(polynomial, 10, 5, 0.1), "\n")

print("(5.2)")
polynomial = [-2.3, 7, -6, 4]
print(bisection(polynomial, 1, 0, 0.1))
print(false_position(polynomial, 1, 0, 0.1), "\n")

print("(5.3)")
polynomial = [-26, 85, -91, 44, -8, 1]
print(bisection(polynomial, 1, 0.5, 0.1))
print(false_position(polynomial, 1, 0, 0.002), "\n")

print("(5.8)")
polynomial = [-18, 0, 1]
print(bisection(polynomial, 5, 4, 0.005))
print(false_position(polynomial, 5, 4, 0.005), "\n")

print("(5.12)")
polynomial = [1, 12, 0, 0 -1.6, 0, -2]
polynomial_prime = [12, 0, 0, -6.4, 0, -12]
root, error = bisection(polynomial_prime, 1, 0, 0.05)
print(f(polynomial, root))

