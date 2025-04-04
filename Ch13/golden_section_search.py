import numpy as np

golden_ratio = (np.sqrt(5) - 1)/2

def f(x):
    return 2*np.sin(x) - (x**2)/10

def golden_section(xl, xu, max_it):
    iterations = 0
    while max_it > iterations:
        d = golden_ratio*(xu - xl)
        x1 = xl + d
        x2 = xu - d
        if f(x1) > f(x2):
            xl = x2
        elif f(x1) < f(x2):
            xu = x1
        iterations += 1
    if f(x1) > f(x2): 
        return x1, f(x1)
    else: 
        return x2, f(x2)
        
