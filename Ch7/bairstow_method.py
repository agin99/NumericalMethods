import numpy as np
from poly_comp import evaluate_poly

def poly_mul(p1, p2):
    poly_result = []
    for index_i, i in enumerate(p1):
        for index_j, j in enumerate(p2):
            poly_result_index = index_i + index_j
            component_val = i * j
            if poly_result_index > len(poly_result) - 1: 
                poly_result.append(component_val)
            else: 
                poly_result[poly_result_index] += component_val
    return poly_result

def poly_div(p1, p2):
    poly_result = []
    for i in p1:
        poly_result.append(0)
    for index_i, i in enumerate(p1[::-1]):
        index_1 = len(p1) - index_i - 1
        index_2 = len(p2) - 1
        if len(p2) > len(p1) - index_i: 
            continue
        component_mul = p1[index_1]/p2[-1]
        for index_j in range(len(p2)):
            p1[index_1 - index_j] -= component_mul*p2[index_2 - index_j]
            poly_result[index_1 - index_2] = component_mul
    return poly_result, p1[:len(p2)]

def compute_b(poly, r, s):
    b = []
    for index, i in enumerate(poly[::-1]):
        if index == 0:
            b.insert(0, i)
        elif index == 1:
            b.insert(0, i + b[0]*r)
        else: 
            b.insert(0, i + b[0]*r + b[1]*s)
    return b

def compute_c(b, r, s):
    c = []
    for index, i in enumerate(b[:0:-1]):
        if index == 0:
            c.insert(0, i)
        elif index == 1: 
            c.insert(0, i + c[0]*r)
        else:
            c.insert(0, i + c[0]*r + c[1]*s)
    return c

def solve_system(b, c): 
    ds = (-(c[0]/c[1])*b[1] + b[0])/((c[0]/c[1])*c[2] - c[1])
    dr = (-b[1] - c[2]*ds)/c[1]
    return dr, ds

def handle_root(r, s): 
    x1, x2 = [], []
    if r**2 + 4*s <= 0:
        x1 = [r/2, np.sqrt(-(r**2 + 4*s))/2]
        x2 = [r/2, -np.sqrt(-(r**2 + 4*s))/2]
    else: 
        x1 = [(r + np.sqrt(r**2 + 4*s)) / 2, 0]
        x2 = [(r - np.sqrt(r**2 + 4*s)) / 2, 0]
    return x1, x2

def bairstow_root_finder(poly, r, s, e_s_r, e_s_s, max_it): 
    iterations = 0
    while iterations < max_it:
        b = compute_b(poly, r, s)
        c = compute_c(b, r, s)
        print(c)
        dr, ds = solve_system(b, c)
        r += dr
        s += ds
        e_a_r = abs(dr/r)
        e_a_s = abs(ds/s)
        if e_a_r < e_s_r and e_a_s < e_s_s: 
            return r, s
        iterations += 1

def bairstow_method(poly, r, s, e_s_r, e_s_s, max_it):
    iterations = 0
    roots = []
    while iterations < max_it:
        print(roots)
        print(f"Poly: {poly} {len(poly) - 1} r: {r} s:{s}")
        if len(poly) - 1 == 2:
            x1, x2 = handle_root(poly[1], poly[0])
            roots.append(x1)
            roots.append(x2)
            return roots
            # return r, s, r1, r2
        elif len(poly) - 1 == 1:
            roots.append([-poly[0]/poly[1], 0])
            return roots
            # return r, s, -s/r
        r, s = bairstow_root_finder(poly, r, s, e_s_r, e_s_s, max_it)
        x1, x2 = handle_root(r, s)
        roots.append(x1)
        roots.append(x2)
        poly = poly_div(poly, [-s, -r, 1])
        poly = poly[0]
        del poly[-2:]
        iterations += 1
    return roots
