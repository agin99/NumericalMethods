import matplotlib.pyplot as plt

def f(x):
    return x**3 - 5*x**2 + 7*x - 3

def f_prime_1(x):
    return 3*x**2 - 10*x + 7

def f_prime_2(x):
    return 6*x - 10

def newton_raphson(x, e_s):
    x_0 = x
    x_i = 0
    e_a = 1
    while True:
        x_i = x_0 - f(x_0)*f_prime_1(x_0)/((f_prime_1(x_0))**2 - f(x_0)*f_prime_2(x_0))
        e_a = abs((x_i - x_0) / x_i)
        if e_a < e_s:
            return x_i, e_a
        x_0 = x_i

x_r, e_a = newton_raphson(0, 10**(-5))
print(x_r)
x_r, e_a = newton_raphson(4, 10**(-5))
print(x_r)