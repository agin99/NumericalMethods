from Ch8.molal_volume import van_der_waals_poly, ideal_gas_law 
from Ch8.h2o_dissociation import dissociation_poly
from Ch6.poly_ops import derivative
from Ch6.newton_raphson import newton_raphson

def molal_volume_comp():
    p = 2.5
    a = 14.09
    b = 0.0994
    T = 400
    f_out = van_der_waals_poly(p, a, b, T)
    V_i = ideal_gas_law(p, T)
    f, f_prime = f_out[0], f_out[1]
    V_r, e_a = newton_raphson(f, f_prime, V_i, 0.001)
    return V_r, e_a

def h2o_dis():
    K = 0.05
    p_t = 3
    x_i = 0.1
    dis_poly = dissociation_poly(K, p_t)
    dis_poly_prime = derivative(dis_poly)
    x_r, e_a = newton_raphson(dis_poly, dis_poly_prime, x_i, 0.000001)
    return x_r, e_a
    
x_r, e_a = h2o_dis()
print(f"Root: {x_r:.5f}")
print(f"Error: {e_a}")