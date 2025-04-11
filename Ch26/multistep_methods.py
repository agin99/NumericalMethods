import numpy as np

def predictor(func, y0, xi, yi, step_size): 
    return y0 + func(xi, yi)*2*step_size 

def corrector(func, xi, yi, y1, step_size, tol): 
    e_a = np.inf
    prev_y1 = 0
    while e_a > tol: 
        y1 = yi + (func(xi, yi) + func(xi + step_size, y1)) / 2 * step_size
        e_a = abs((y1 - prev_y1) / y1)
        prev_y1 = y1
    return y1

def nss_heuns_method(func, xi, xf, y0, yi, step_size, tol):
    xy = []
    while xi <= xf: 
        xy.append((xi, yi))
        y1 = predictor(func, y0, xi, yi, step_size)
        y1 = corrector(func, xi, yi, y1, step_size, tol)
        y0 = yi
        yi = y1
        xi += step_size
    return xy

func = lambda x, y: 4*np.pow(np.e, 0.8*x) - 0.5*y
xi = 0
xf = 4
y0 = -0.3929953
yi = 2
step_size = 1
tol = 10**(-5)
print(nss_heuns_method(func, xi, xf, y0, yi, step_size, tol))