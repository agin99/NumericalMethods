import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.pow(np.e, -x) - x 

def f_prime(x):
    return -np.pow(np.e, -x) - x

def newton_raphson(x_i, e_s):
    prev_x = 0
    x_r = x_i
    e_a = 1
    while True: 
        x_r = x_r - f(x_r)/f_prime(x_r)
        e_a = abs(x_r - prev_x) / x_r
        prev_x = x_r
        if e_a < e_s:
            return x_r, e_a
        
x_r, e_a = newton_raphson(0, 10**(-9))
print(f"Error: {e_a}")
print(f"Root: {x_r}")