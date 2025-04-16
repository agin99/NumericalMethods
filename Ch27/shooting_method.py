import numpy as np

def compute_k_vals(funcs, xi, yi, step_size):
    k1 = []
    for f in funcs: 
        k1.append(f(xi, yi))
    y_ = [i + j*1/2*step_size for i, j in zip(yi, k1)]
    k2 = []
    for f in funcs: 
        k2.append(f(xi + 1/2*step_size, y_))
    y_ = [i + j*1/2*step_size for i, j in zip(yi, k2)]
    k3 = []
    for f in funcs: 
        k3.append(f(xi + 1/2*step_size, y_))
    y_ = [i + j*step_size for i, j in zip(yi, k3)]
    k4 = []
    for f in funcs: 
        k4.append(f(xi + step_size, y_))
    return k1, k2, k3, k4

def increment_y_vals(k, yi, step_size):
    i = 0
    while i < len(yi):
        yi[i] = yi[i] + 1/6 * (k[0][i] + 2*k[1][i] + 2*k[2][i] + k[3][i]) * step_size
        i += 1
    return yi

def adaptive_rk_step(step_size, funcs, xi, yi, tol, max_it):
    delta = []
    e_a = np.inf
    half_step = step_size / 2
    while True:
        k_full = compute_k_vals(funcs, xi, yi.copy(), step_size)
        y_full = increment_y_vals(k_full, yi.copy(), step_size)
        k_half = compute_k_vals(funcs, xi, yi.copy(), half_step)
        y_half = increment_y_vals(k_half, yi.copy(), half_step)
        k_half = compute_k_vals(funcs, xi + half_step, y_half.copy(), half_step)
        y_half = increment_y_vals(k_half, y_half.copy(), half_step)
        delta = [j - i for i, j in zip(y_full, y_half)]
        e_a = np.sqrt(sum([i**2 for i in delta])) / 15
        if tol > e_a: 
            y_corr = [i + j/15 for i, j in zip(y_half, delta)]
            return y_corr, step_size
        step_size = half_step
        half_step /= 2

def solve_system_RK(step_size, funcs, xi, xf, yi, tol, max_it): 
    y = []
    i = 0
    temp_step_size = 0
    while xi <= xf:
        y.append(yi.copy())
        yi, temp_step_size = adaptive_rk_step(step_size, funcs, xi, yi, tol, max_it)
        xi += temp_step_size
        i += 1
    return y

def linear_shooting_method(step_size, funcs, xi, xf, yi, yf, tol, max_it):
    e_a = np.inf
    i = 0
    while e_a > tol and max_it > i:
        adjusted_y = yi.copy()
        y = solve_system_RK(step_size, funcs, xi, xf, yi, tol, max_it)
        x1, y1 = yi[1], y[-1][0]
        x2, y2 = 0, 0
        adjusted_y_output = 0
        if y[-1][0] < yf:
            adjusted_y_output = y[-1][0]
            while adjusted_y_output < yf:
                adjusted_y[1] = 2*yi[1]
                adjusted_y_output = solve_system_RK(step_size, funcs, xi, xf, adjusted_y, tol, max_it)[-1][0]
                x2, y2 = adjusted_y[1], adjusted_y_output
        elif y[-1][0] > yf:
            adjusted_y_output = y[-1][0]
            while adjusted_y_output > yf:
                adjusted_y[1] = yi[1] / 2
                adjusted_y_output = solve_system_RK(step_size, funcs, xi, xf, adjusted_y, tol, max_it)[-1][0]
                x2, y2 = adjusted_y[1], adjusted_y_output
        yi[1] = yi[1] + (x2 - x1) / (y2 - y1) * (yf - y1)
        y = solve_system_RK(step_size, funcs, xi, xf, yi, tol, max_it)
        e_a = abs((y[-1][0] - yf) / y[-1][0])
        i += 1
    return y

def generate_guess_set(step_size, funcs, xi, xf, yi, yf, tol, max_it): 
    s0 = yi[1]
    T0 = solve_system_RK(step_size, funcs, xi, xf, yi, tol, max_it)[-1][0]
    s1 = s0*2 if T0 < yf else s0/2
    T1 = solve_system_RK(step_size, funcs, xi, xf, [yi[0], s1], tol, max_it)[-1][0]
    s2 = 0.5*(s0 + s1)
    T2 = solve_system_RK(step_size, funcs, xi, xf, [yi[0], s2], tol, max_it)[-1][0]
    return [s0,T0], [s1,T1], [s2,T2]
    
def quadratic_interpolation(x1, y1, x2, y2, x3, y3):
    a = ((y3 - y2) / (x3 - x2) - (y2 - y1) / (x2 - x1)) / (x3 - x1)
    b = ((y2 - y1) / (x2 - x1)) - a * (x2 + x1)
    c = y1 - a*x1**2 - b*x1
    return [c, b, a]

def evaluate_poly(poly, x):
    poly_sum = 0
    for index, i in enumerate(poly[len(poly)::-1]):
        poly_index = len(poly) - index - 1
        poly_sum = poly_sum * x + poly[poly_index]
    return poly_sum

def bisection(f, poly, x_u, x_l, e_s, max_it): 
    prev_x_r = 0
    e_a = np.inf
    j = 0
    while max_it > j:
        x_r = (x_u + x_l) / 2
        if f(poly, x_r)*f(poly, x_l) < 0:
            x_u = x_r
        elif f(poly, x_r)*f(poly, x_l) > 0: 
            x_l = x_r
        e_a = abs(x_r - prev_x_r)
        if e_a < e_s:
            return x_r, e_a
        prev_x_r = x_r
        j += 1
    return x_r, e_a

def quadratic_shooting_method(step_size, funcs, xi, xf, yi, yf, tol, max_it): 
    e_a = np.inf
    i = 0
    adj_y0, adj_y1, adj_y2 = generate_guess_set(step_size, funcs, xi, xf, yi, yf, tol, max_it)
    sorted_s_vals = sorted([l[0] for l in [adj_y0, adj_y1, adj_y2]])
    while e_a > tol and max_it > i:
        adj_y0 = solve_system_RK(step_size, funcs, xi, xf, [yi[0], sorted_s_vals[0]], tol, max_it)[-1][0]
        adj_y1 = solve_system_RK(step_size, funcs, xi, xf, [yi[0], sorted_s_vals[1]], tol, max_it)[-1][0]
        adj_y2 = solve_system_RK(step_size, funcs, xi, xf, [yi[0], sorted_s_vals[2]], tol, max_it)[-1][0]
        poly = quadratic_interpolation(sorted_s_vals[0], adj_y0, sorted_s_vals[1], adj_y1, sorted_s_vals[2], adj_y2)
        poly[0] -= yf
        r, _ = bisection(evaluate_poly, poly, sorted_s_vals[2], sorted_s_vals[0], tol, max_it)
        sorted_s_vals.append(r)
        sorted_s_vals = sorted(sorted_s_vals)
        index = sorted_s_vals.index(r)
        if index == 0:
            sorted_s_vals = sorted_s_vals[:3]
        elif index == len(sorted_s_vals)-1:
            sorted_s_vals = sorted_s_vals[-3:]
        else:
            sorted_s_vals = sorted_s_vals[index-1:index+2]
        i += 1
    return sorted_s_vals[1], adj_y1

T_a = 20
T_f = 200
h_prime_1 = 0.01
h_prime_2 = 5 * 10**(-8)
dT_dx = lambda dummy, y: y[1]
dz_dx_1 = lambda dummy, y: h_prime_1*(y[0] - T_a)
dz_dx_2 = lambda dummy, y: h_prime_2*(y[0] - T_a)**4
xi = 0
xf = 10
yi = [40, 10]
step_size = 2
max_it = 100
tol = 10**(-5)
# y = linear_shooting_method(step_size, [dT_dx, dz_dx_1], xi, xf, yi, T_f, tol, max_it)
y = quadratic_shooting_method(step_size, [dT_dx, dz_dx_2], xi, xf, yi, T_f, tol, max_it)
print(y)