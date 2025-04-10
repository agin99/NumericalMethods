import numpy as np
import matplotlib.pyplot as plt

def eulers_method(step_size, xi, xf, yi, f_prime): 
    y = []
    intervals = (xf - xi) / step_size
    i = 0
    while i <= intervals: 
        x = xi + i * step_size
        y.append(yi)
        yi += f_prime(x, yi) * step_size
        i += 1
    return y

def heuns_method(step_size, xi, xf, yi, f_prime, corr_it):
    y = []
    intervals = (xf - xi) / step_size
    i = 0
    while i < intervals: 
        x = xi + i * step_size
        yi10 = yi + f_prime(x, yi)*step_size
        for j in range(corr_it): 
            if j == 0: 
                yi1 = yi + (f_prime(x, yi) + f_prime(x + step_size, yi10)) / 2 * step_size
            else: 
                yi1 = yi + (f_prime(x, yi) + f_prime(x + step_size, yi1)) / 2 * step_size
        y.append(yi1)
        yi = yi1
        i += 1
    return y

def midpoint_method(step_size, xi, xf, yi, f_prime):
    y = []
    intervals = (xf - xi) / step_size
    i = 0
    while i <= intervals: 
        x = xi + i * step_size
        y.append(yi)
        x_mid = x + step_size / 2
        y_mid = yi + f_prime(x, yi) * step_size / 2
        yi += f_prime(x_mid, y_mid) * step_size
        i += 1
    return y
    
f_prime = lambda x, y: 4*np.pow(np.e, 0.8*x) - 0.5*y
xi = 0
xf = 4
yi = 2
step_size = 1
y = heuns_method(step_size, xi, xf, yi, f_prime, 15)
y = midpoint_method(step_size, xi, xf, yi, f_prime)