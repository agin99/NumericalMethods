import math
import numpy as np
import matplotlib.pyplot as plt
from poly_ops import format_poly, evaluate_poly

def quadratic_interpolation(x1, y1, x2, y2, x3, y3):
    a = ((y3 - y2) / (x3 - x2) - (y2 - y1) / (x2 - x1)) / (x3 - x1)
    b = ((y2 - y1) / (x2 - x1)) - a * (x2 + x1)
    c = y1 - a*x1**2 - b*x1
    return [c, b, a]

def iqi_root_finder(x1, y1, x2, y2, x3, y3, e_s, max_it):
    x_r = 0
    prev_x_r = x3
    e_a = 1
    it_tracker = 0
    while True:
        norm_poly = quadratic_interpolation(x1, y1, x2, y2, x3, y3)
        iqi_poly = quadratic_interpolation(y1, x1, y2, x2, y3, x3)
        # x1 = evaluate_poly(iqi_poly, y1)
        # x2 = evaluate_poly(iqi_poly, y2)
        # x3 = evaluate_poly(iqi_poly, y3)
        # x_r = ((y2*y3)/((y1 - y2)*(y1 - y3)))*x1
        # x_r += ((y1*y3)/((y2 - y1)*(y2 - y3)))*x2
        # x_r += ((y1*y2)/((y3 - y1)*(y3 - y2)))*x3
        x_r = evaluate_poly(iqi_poly, 0)
        y_r = evaluate_poly(norm_poly, x_r)
        x1, y1 = x2, y2
        x2, y2 = x3, y3
        x3, y3 = x_r, y_r
        e_a = abs((x_r - prev_x_r) / x_r)
        if e_a < e_s or it_tracker == max_it:
            return x_r, e_a
        prev_x_r = x_r

def brent_method():
    pass

quadratic = quadratic_interpolation(1, 2, 2, 1, 4, 5)
formatted_quadratic = ("").join(format_poly(quadratic))
print(formatted_quadratic)
inverse_quadratic = quadratic_interpolation(2, 1, 1, 2, 5, 4)
formatted_inverse = ("").join(format_poly(inverse_quadratic))
print(formatted_inverse)

print(iqi_root_finder(1, 2, 2, 1, 4, 5, 1, 10))