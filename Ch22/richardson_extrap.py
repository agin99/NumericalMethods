import numpy as np

def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def trapezoidal(intervals, func, a, b):
    trap_rule = lambda func, a_, b_: (b_ - a_)*(func(a_) + func(b_))/2
    I_tot = 0
    start = a
    end = b
    interval_size = (end - start) / intervals
    for i in range(intervals):
        a = start + i * interval_size
        b = a + interval_size
        I_tot += trap_rule(func, a, b)
    return I_tot

def unequal_segment_trapezoidal(func, xi): 
    segments = [[i, j] for i, j in zip(xi[:-1], xi[1:])]
    I = 0
    for i in segments:
        I += trapezoidal(len(i) - 1, func, i[0], i[1])
    return I

def compute_error_term():
    pass

def richardson_extrap(intervals_1, intervals_2, func, a, b):
    I1 = trapezoidal(intervals_1, func, a, b)
    I2 = trapezoidal(intervals_2, func, a, b)
    if intervals_2 == 2*intervals_1:
        return 4/3 * I2 - 1/3 * I1
    else: 
        return I2 + 1/(2**2 - 1)*(I2 - I1)
    
def romberg_integration(intervals, func, a, b): 
    I = []
    for i in range(1, len(intervals)): 
        I.append(richardson_extrap(intervals[i-1], intervals[i], func, a, b))
    if len(intervals) < 4:
        return I[-1]
    index = 3
    I0 = []
    while True: 
        for I_index in range(len(I) - 1):
            I_ = (4**(index - 1)*I[I_index + 1] - I[I_index]) / (4**(index - 1) - 1)
            I0.append(I_)
        I = I0
        if len(I) == 1: 
            break
        I0 = []
        index += 1
    return I[0]

a = 0
b = 0.8
# print(richardson_extrap(1, 2, f, 0, 0.8))
# print(richardson_extrap(2, 4, f, 0, 0.8))
I = romberg_integration([1, 2, 4], f, a, b)
print(I)