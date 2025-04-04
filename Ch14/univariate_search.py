import numpy as np

golden_ratio = (np.sqrt(5) - 1)/2

def f(x,y):
    return y - x - 2*x**2 - 2*x*y - y**2

def golden_section_x(xl, xu, y, tol, max_it):
    iterations = 0
    while max_it > iterations:
        d = golden_ratio*(xu - xl)
        x1 = xl + d
        x2 = xu - d
        if f(x1, y) > f(x2, y):
            xl = x2
        elif f(x1, y) < f(x2, y):
            xu = x1
        iterations += 1
    if f(x1, y) > f(x2, y): 
        return x1, f(x1, y)
    else: 
        return x2, f(x2, y)
    
def golden_section_y(yl, yu, x, tol, max_it):
    iterations = 0
    while max_it > iterations:
        d = golden_ratio*(yu - yl)
        y1 = yl + d
        y2 = yu - d
        if f(x, y1) > f(x, y2):
            yl = y2
        elif f(x, y1) < f(x, y2):
            yu = y1
        iterations += 1
    if f(x, y1) > f(x, y2): 
        return y1, f(x, y1)
    else: 
        return y2, f(x, y2)

def univariate_search(xl, xu, yl, yu, tol, max_it):
    x_active = True
    x = 0
    y = 0
    f_xy = 0
    iterations = 0 
    while iterations < max_it: 
        prev_f_xy = f_xy
        if x_active: 
            x, f_xy = golden_section_x(xl, xu, y, tol, max_it)
            print(x, y, f_xy)
            x_active = False
        else: 
            y, f_xy = golden_section_y(yl, yu, x, tol, max_it)
            print(x, y, f_xy)
            x_active = True
        if abs((f_xy - prev_f_xy) / f_xy) < tol:
            return x, y, f_xy
        iterations += 1
    return x, y, f_xy