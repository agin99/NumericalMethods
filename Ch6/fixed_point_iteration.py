import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.pow(np.e, -x)

def fixed_point_it(e_s):
    e_a = 1
    x_r = 0
    prev_x_r = 0
    while True:
        x_r = f(x_r)
        e_a = abs(x_r - prev_x_r)/x_r
        if e_a < e_s:
            return x_r, e_a
        prev_x_r = x_r

x = np.linspace(0, 1, 100)
y = x
f_x = [f(i) for i in x]
x_r, e_a = fixed_point_it(0.000001)
plt.plot(x, y)
plt.plot(x, f_x)
plt.plot([x_r, x_r], [0, f(x_r)], 'k--')
plt.plot(x_r, f(x_r), 'ro')
plt.text(x_r + 0.05, f(x_r), f"({x_r:.3f}, {f(x_r):.3f})")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Fixed Point Iteration f(x) = e^(-x)')
plt.show()