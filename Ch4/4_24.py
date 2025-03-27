import math
import numpy as np

def f_exact(x):
    return np.sin(x)

def f_approx(es, max_it, x): 
    prev_approx = 0
    order = 1
    while True:
        sin_approx = 0
        for i in range(order):
            next_term = np.pow(x, 2*i + 1) / math.factorial(2*i + 1)
            if i % 2 == 0:
                sin_approx += next_term
            else: 
                sin_approx -= next_term
        e_approx = abs((sin_approx - prev_approx) / sin_approx)
        e_true = abs((f_exact(x) - sin_approx) / f_exact(x))
        if e_approx < es or order == max_it: 
            return e_true, e_approx, sin_approx, order
        prev_approx = sin_approx
        order += 1

def main():
    e_true, e_approx, sin_approx, order = f_approx(0.000001, 100, np.pi/6)
    print(f"True relative error: {e_true}")
    print(f"Approxmiate relative error: {e_approx}")
    print(f"Approx sine: {sin_approx}")
    print(f"Final order: {order}")
    print(f"Exact sine: {f_exact(np.pi/6)}")
main()