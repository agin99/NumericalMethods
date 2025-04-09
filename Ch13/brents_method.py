import numpy as np
from golden_section_search import golden_section, golden_ratio

def f(x):
    return 2*np.sin(x) - (x**2)/10

def single_it_golden_search(xl, xu):
    d = golden_ratio*(xu - xl)
    x1 = xl + d
    x2 = xu - d
    if f(x1) > f(x2):
        xl = x2
    elif f(x1) < f(x2):
        xu = x1
    return x1, x2

def para_interpolation(x, tol, max_it):
    iterations = 0 
    prev_interval_size = abs(x[-1] - x[0])
    while iterations < max_it:
        x0 = x[0]
        x1 = x[1]
        x2 = x[2]
        x3 = (
                f(x0)*(x1**2 - x2**2) + f(x1)*(x2**2 - x0**2) + f(x2)*(x0**2 - x1**2)
            )/(
                2*f(x0)*(x1 - x2) + 2*f(x1)*(x2 - x0) + 2*f(x2)*(x0 - x1)
            )
        for i in range(len(x)-1):
            if x3 > x[i] and x3 < x[i+1]:
                x = [x[i], x3, x[i+1]]
        interval_size = abs(x[-1] - x[0])
        if (x[0] > x3 or x3 > x[-1]) or interval_size > prev_interval_size: 
            return False, x[0], x[2]
        if (abs(x3 - x[0]) < tol) and (abs(x3 - x[-1]) < tol): 
            return True, x3, f(x[1])
        prev_interval_size = interval_size
        iterations += 1
    return True, x[1], f(x[1])
        
def brents_method(xl, xu, tol, max_it):
    success = False
    iterations = 0 
    while iterations < max_it: 
        x = [xl, (xl + xu)/2, xu]
        success, x1, x2 = para_interpolation(x, tol, max_it)
        if success: 
            return x1, f(x1)
        xl, xu = single_it_golden_search(x1, x2)
        iterations += 1
    return x, f(x)

x, f_x = brents_method(0, 4, 10**(-5), 5)
print(f"f({x:.5f}) = {f_x:5f}")