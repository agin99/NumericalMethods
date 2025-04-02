import numpy as np
from Ch7.poly_comp import evaluate_poly

def f(x):
    return np.pow(np.e, -x) - x 

def f_prime(x):
    return -np.pow(np.e, -x) - x

def newton_raphson(f, f_prime, x_i, e_s):
    prev_x = 0
    x_r = x_i
    e_a = 1
    while True: 
        x_r = x_r - evaluate_poly(f, x_r)/evaluate_poly(f_prime, x_r)
        e_a = abs(x_r - prev_x) / x_r
        prev_x = x_r
        if e_a < e_s:
            return x_r, e_a