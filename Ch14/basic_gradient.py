import numpy as np
from univariate_search import univariate_search

def f(x, y):
    return 5 - (x - 1)**4 - (y - 1)**4

def finite_difference_approx(func, x, y, delta):
    df_dx = (func(x + delta, y) - func(x - delta, y)) / (2*delta)
    df_dy = (func(x, y + delta) - func(x, y - delta)) / (2*delta)
    return df_dx, df_dy

def gradient_ascent(func, x, y, tol, max_it):
    h = 0.01
    for i in range(max_it):
        df_dx, df_dy = finite_difference_approx(func, x, y, 10**(-5))
        grad_norm = np.sqrt(df_dx**2 + df_dy**2) 
        if grad_norm < tol:
            return x, y, func(x, y)
        x_new = x + df_dx*h
        y_new = y + df_dy*h
        if(x_new == x) and (y_new == y):
            return(x, y, func(x, y))
        x, y = x_new, y_new
    return x, y, func(x, y)
    
x, y, f_xy = gradient_ascent(f, -2, 3, 10**(-4), 1000)
print(f"f({x:.4f}, {y:.4f}) = {f_xy:.4f}")