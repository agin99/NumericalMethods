import random
import numpy as np

golden_ratio = (np.sqrt(5) - 1)/2

def golden_section(f, xl, xu, max_it):
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

def monte_carlo_integration(func, a, b, n, max_it): 
    _, f_max = golden_section(func, a, b, max_it)
    num_under_curve = 0
    for i in range(n):
        x = a + (b - a) * random.random()
        y = f_max * random.random()
        if y < func(x):
            num_under_curve += 1 
    return num_under_curve / n * (b - a) * f_max

func = lambda x: 400*x**5 - 900*x**4 + 675*x**3 - 200*x**2 + 25*x + 0.2
a = 0 
b = 0.8
n = 100_000
iterations = 100
I = monte_carlo_integration(func, a, b, n, iterations)
print(I)