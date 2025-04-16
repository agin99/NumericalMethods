import numpy as np

def one_step_euler(step_size, xi, yi, f_prime): 
    y = []
    for i, j in zip(yi, f_prime):
        y.append(i + j(xi, yi) * step_size)
    return y

def solve_system_euler(step_size, xi, xf, yi, f_prime):
    intervals = (xf - xi) / step_size
    y = []
    i = 0
    while i <= intervals:
        y.append(yi)
        yi = one_step_euler(step_size, xi, yi, f_prime)
        xi += step_size
        i += 1
    return y

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

def adaptive_rk_step(step_size, funcs, xi, yi, tol):
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

def solve_system_RK(step_size, funcs, xi, xf, yi, tol): 
    y = []
    i = 0
    while xi <= xf:
        y.append(yi.copy())
        yi, step_size = adaptive_rk_step(step_size, funcs, xi, yi, tol)
        xi += step_size
        i += 1
    return y

f_prime_1 = lambda x, y: -0.5*y[0]
f_prime_2 = lambda x, y: 4 - 0.3 * y[1] - 0.1 * y[0]
xi = 0
xf = 2
yi = [4, 6]
step_size = 0.5
tol = 10**(-2)
y = solve_system_RK(step_size, [f_prime_1, f_prime_2], xi, xf, yi, tol)
print(y)

f_prime_3 = lambda x, y: 4 * np.pow(np.e, 0.8 * x) - 0.5 * y[0]
xi = 0
xf = 2
yi = [2]
step_size = 2
tol = 10**(-2)
y = solve_system_RK(step_size, [f_prime_3], xi, xf, yi, tol)
print(y)