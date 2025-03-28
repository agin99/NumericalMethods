import math
import numpy as np
import matplotlib.pyplot as plt
from poly_ops import format_poly

def quadratic_interpolation(x1, y1, x2, y2, x3, y3):
    a = ((y3 - y2) / (x3 - x2) - (y2 - y1) / (x2 - x1)) / (x3 - x1)
    b = ((y2 - y1) / (x2 - x1)) - a * (x2 + x1)
    c = y1 - a*x1**2 - b*x1
    return [c, b, a]

def inverse_quadratic_interpolation(x1, y1, x2, y2, x3, y3):
    return quadratic_interpolation(y1, x1, y2, x2, y3, x3)

def brent_method():
    pass

quadratic = quadratic_interpolation(1, 2, 2, 1, 4, 5)
formatted_quadratic = ("").join(format_poly(quadratic))
print(formatted_quadratic)
inverse_quadratic = inverse_quadratic_interpolation(1, 2, 2, 1, 4, 5)
formatted_inverse = ("").join(format_poly(inverse_quadratic))
print(formatted_inverse)
