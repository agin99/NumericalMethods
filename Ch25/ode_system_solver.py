import numpy as np
from eulers_method import eulers_method

def one_step_euler(step_size, xi, yi, f_prime): 
    y = []
    for i, j in zip(yi, f_prime):
        y.append(i + j(xi, yi) * step_size)
    return y

def solve_system_euler(step_size, xi, xf, yi, f_prime):
    intervals = (xf - xi) / step_size
    y = []
    i = 0
    while i <= intervals:
        y.append(yi)
        yi = one_step_euler(step_size, xi, yi, f_prime)
        xi += step_size
        i += 1
    return y

def compute_k_vals(func, xi, yi, step_size):
    k1 = []
    for f in func: 
        k1.append(f(xi, yi))
    y_ = [i + j*1/2*step_size for i, j in zip(yi, k1)]
    k2 = []
    for f in func: 
        k2.append(f(xi + 1/2*step_size, y_))
    y_ = [i + j*1/2*step_size for i, j in zip(yi, k2)]
    k3 = []
    for f in func: 
        k3.append(f(xi + 1/2*step_size, y_))
    y_ = [i + j*step_size for i, j in zip(yi, k3)]
    k4 = []
    for f in func: 
        k4.append(f(xi + step_size, y_))
    return k1, k2, k3, k4

def increment_y_vals(k, yi, step_size):
    i = 0
    while i < len(yi):
        yi[i] = yi[i] + 1/6 * (k[0][i] + 2*k[1][i] + 2*k[2][i] + k[3][i]) * step_size
        i += 1
    return yi

def solve_system_RK(step_size, xi, xf, yi, f_prime): 
    intervals = (xf - xi) / step_size
    k = []
    y = []
    i = 0
    while i < intervals:
        y.append(yi[:])
        k = compute_k_vals(f_prime, xi, yi, step_size)
        yi = increment_y_vals(k, yi, step_size)
        xi += step_size
        i += 1
    return y

f_prime_1 = lambda x, y: -0.5*y[0]
f_prime_2 = lambda x, y: 4 - 0.3 * y[1] - 0.1 * y[0]
xi = 0
xf = 2
yi = [4, 6]
step_size = 0.5
y_euler = solve_system_euler(step_size, xi, xf, yi, [f_prime_1, f_prime_2])
y_rk = solve_system_RK(step_size, xi, xf, yi, [f_prime_1, f_prime_2])