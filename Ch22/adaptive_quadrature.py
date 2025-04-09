import numpy as np

def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def simpsons_13(intervals, func, a, b):
    num_tot = 0
    start = a
    end = b
    interval_size = ((end*100 - start*100) / intervals) / 100
    for i in range(1, intervals):
        if i % 2 == 0: 
            num_tot += 2 * func(start + i * interval_size)
        else: 
            num_tot += 4 * func(start + i * interval_size)
    return (b - a)*(func(a) + num_tot + func(b))/(3*intervals)

def adaptive_quadrature(intervals, func, a, b, tol): 
    e_a = None
    interval_size = (b - a) / intervals
    I = 0
    for i in range(intervals):
        a0 = a + i * interval_size
        b0 = a0 + interval_size
        specific_intervals = intervals
        while True:
            I1 = simpsons_13(specific_intervals, func, a0, b0)
            I2 = simpsons_13(specific_intervals*2, func, a0, b0)
            e_a = abs(I2 - I1)
            if e_a < tol: 
                I += I2
                break
            specific_intervals *= 2
    return I

intervals = 2
a = 0
b = 0.8
tol = 10**(-4)
I = adaptive_quadrature(intervals, f, a, b, tol)
print(I)
