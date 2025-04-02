#acetone (a=14.09, b=0.0994, T=400K, p=2.5atm)
#R = 0.08206
#molal volume

from Ch7.poly_comp import evaluate_poly

R = 0.08206

def ideal_gas_law(p, T):
    return R*T/p

def van_der_waals_poly(p, a, b, T):
    return [[-a*b, a, -(p*b + R*T), p], [a, -2*(p*b + R*T), 3*p]]