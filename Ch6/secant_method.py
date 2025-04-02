import numpy as np

def f(x):
    return np.pow(np.e, -x) - x 

def secant_method(x_0, x_i, e_s):
    x_r = x_i - f(x_i)*(x_0 - x_i)/(f(x_0) - f(x_i))
    e_a = 1
    while True: 
        x_0 = x_i
        x_i = x_r
        x_r = x_i - f(x_i)*(x_0 - x_i)/(f(x_0) - f(x_i))
        e_a = abs(x_r - x_i) / x_r
        if e_a < e_s:
            return x_r, e_a