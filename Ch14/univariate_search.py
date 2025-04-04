import numpy as np

golden_ratio = (np.sqrt(5) - 1)/2

def f(x,y):
    return -[100*(y - x**2)**2 + (1-x)**2]

def golden_section_x(func, xl, xu, y, tol, max_it):
    iterations = 0
    d = golden_ratio*(xu - xl)
    x1 = xl + d
    x2 = xu - d
    while max_it > iterations and abs(xu - xl) > tol:
        if func(x1, y) > func(x2, y):
            xl = x2
        elif func(x1, y) < func(x2, y):
            xu = x1
        d = golden_ratio*(xu - xl)
        x1 = xl + d
        x2 = xu - d
        iterations += 1
    if func(x1, y) > func(x2, y): 
        return x1, func(x1, y)
    else: 
        return x2, func(x2, y)
    
def golden_section_y(func, yl, yu, x, tol, max_it):
    iterations = 0
    d = golden_ratio*(yu - yl)
    y1 = yl + d
    y2 = yu - d
    while max_it > iterations and abs(yu - yl) > tol:
        d = golden_ratio*(yu - yl)
        y1 = yl + d
        y2 = yu - d
        if func(x, y1) > func(x, y2):
            yl = y2
        elif func(x, y1) < func(x, y2):
            yu = y1
        d = golden_ratio*(yu - yl)
        y1 = yl + d
        y2 = yu - d
        iterations += 1
    if func(x, y1) > func(x, y2): 
        return y1, func(x, y1)
    else: 
        return y2, func(x, y2)

def univariate_search(func, xl, xu, yl, yu, tol, max_it):
    x_active = True
    x = 0
    y = 0
    f_xy = 0
    iterations = 0 
    while iterations < max_it: 
        prev_f_xy = f_xy
        if x_active: 
            x, f_xy = golden_section_x(func, xl, xu, y, tol, max_it)
            x_active = False
        else: 
            y, f_xy = golden_section_y(func, yl, yu, x, tol, max_it)
            x_active = True
        if abs((f_xy - prev_f_xy) / f_xy) < tol:
            return x, y, f_xy
        iterations += 1
    return x, y, f_xy