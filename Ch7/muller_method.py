from poly_comp import evaluate_poly
import numpy as np

def comp_coef(x0, y0, x1, y1, x2, y2):
    h0 = x1 - x0
    h1 = x2 - x1
    d0 = (y1 - y0) / (x1 - x0)
    d1 = (y2 - y1) / (x2 - x1)
    a = (d1 - d0) / (h1 + h0)
    b = (a * h1 + d1)
    c = y2
    return a, b, c

def comp_discriminant(a, b, c):
    return np.sqrt(b**2 - 4*a*c)

def comp_root(poly, x0, x1, x2, es, max_it):
    y0 = evaluate_poly(poly, x0)
    y1 = evaluate_poly(poly, x1)
    y2 = evaluate_poly(poly, x2)
    iterat = 0
    while iterat < max_it:
        a, b, c = comp_coef(x0, y0, x1, y1, x2, y2)
        discr = comp_discriminant(a, b, c)
        denom = 0 
        if b >= 0:
            denom = abs(b + discr)
        else: 
            denom = abs(b - discr)
        x_r = x2 + (-2*c/denom)
        e_a = abs((x_r - x2) / x_r)
        if e_a < es: 
            return x_r, e_a
        x0, y0 = x1, y1
        x1, y1 = x2, y2
        x2, y2 = x_r, evaluate_poly(poly, x_r)
        iterat += 1
    return x_r, e_a