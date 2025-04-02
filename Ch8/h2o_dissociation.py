# H2O <=> H2 + (1/2)O2

from Ch6.poly_ops import poly_mul

def dissociation_poly(k, p_t):
    a = poly_mul(poly_mul([1, -1], [1, -1]), [2, 1])
    poly = [i*(k**2)/(2*p_t) for i in a]
    poly[2] -= 1
    return poly