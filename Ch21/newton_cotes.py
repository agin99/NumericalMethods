import numpy as np
import matplotlib.pyplot as plt

g = 9.8
m = 68.1
c = 12.5

def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x**3 - 900 * x**4 + 400 * x**5

def falling_parachutist(t):
    return g*m/c*(1 - np.pow(np.e, -(c/m)*t))

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

def simpsons_13(intervals, func, a, b):
    num_tot = 0
    start = a
    end = b
    interval_size = ((end*100 - start*100) / intervals) / 100
    num_tot
    for i in range(1, intervals):
        if i % 2 == 0: 
            num_tot += 2 * func(start + i * interval_size)
        else: 
            num_tot += 4 * func(start + i * interval_size)
    return (b - a)*(func(a) + num_tot + func(b))/(3*intervals)

def simpsons_38(intervals, func, a, b):
    num_tot = 0
    start = a
    end = b
    interval_size = (end - start) / (intervals)
    num_tot
    for i in range(1, intervals):
        num_tot += 3 * func(start + i * interval_size)
    return (b - a)*(func(a) + num_tot + func(b))/(8)

def compute_intervals_separation(intervals):
    intervals_13 = 0
    intervals_38 = 0
    if intervals % 2 == 0: 
        intervals_13 = intervals
    elif intervals % 3 == 0: 
        intervals_38 = intervals
    else: 
        if (intervals // 2) % 2 == 0:
            intervals_13 = intervals // 2
            intervals_38 = intervals - intervals_13
        else: 
            intervals_38 = intervals // 2
            intervals_13 = intervals - intervals_38
    return intervals_13, intervals_38

def general_simpsons(intervals, func, a, b):
    intervals_13, intervals_38 = compute_intervals_separation(intervals)
    interval_size = (b - a) / intervals
    I = 0
    if intervals_13 != 0:
        I += simpsons_13(intervals_13, func, a, a + interval_size*intervals_13)
    if intervals_38 != 0:
        I += simpsons_38(intervals_38, func, a + interval_size*(intervals_13), b)
    return I

def separate_segments(xi):
    segments = []
    prev_seg_size = None
    for index, i in enumerate(xi[1:]): 
        seg_size = i*100 - xi[index]*100
        if seg_size == prev_seg_size:
            segments.append([xi[index - 1], xi[index], i])
        else:
            segments.append([xi[index], i])
        prev_seg_size = seg_size
    index = 0
    for i in segments[1:]:
        if i[1]*100 - i[0]*100 == segments[index][-1]*100 - segments[index][-2]*100:
            segments[index + 1][:-1] = segments[index]
            segments.pop(index)
        else:
            index += 1
    return segments

def unequal_segment_trapezoidal(func, xi): 
    segments = [[i, j] for i, j in zip(xi[:-1], xi[1:])]
    I = 0
    for i in segments:
        I += trapezoidal(len(i) - 1, func, i[0], i[1])
    return I

def unequal_segment_general(func, xi):
    segments = separate_segments(xi)
    I = 0
    for i in segments:
        a = i[0]
        b = i[-1]
        print(i)
        if len(i) == 2: 
            I += trapezoidal(len(i) - 1, func, a, b)
        else:
            I += general_simpsons(len(i) - 1, func, a, b)
    return I

def f_x_y(x, y):
    return 2*x*y + 2*x - x**2 - 2*y**2 + 72

def double_integral(func, xi, yi):
    f_y = []
    for y in yi:
        f_x_y_const = lambda x: func(x, y)
        f_y.append(unequal_segment_trapezoidal(f_x_y_const, xi))
    return (yi[-1] - yi[0]) * (f_y[0] + sum([2 * i for i in f_y[1:-1]]) + f_y[-1]) / (2 * (len(xi) - 1))

# I_trap_tot = trapezoidal(100, f, 0, 0.8)
# distance = trapezoidal(10000, falling_parachutist, 0, 10)
# I = general_simpsons(5, f, 0, 0.8)
# xi = [0, 0.12, 0.22, 0.32, 0.36, 0.40, 0.44, 0.54, 0.64, 0.70, 0.80]
# uneq_trap_I = unequal_segment_trapezoidal(f, xi)
# uneq_gen_I = unequal_segment_general(f, xi)
double_I = double_integral(f_x_y, np.linspace(0, 8, 100), np.linspace(0, 6, 100))
print(double_I)