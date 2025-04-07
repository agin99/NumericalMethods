import matplotlib.pyplot as plt
import numpy as np

def compute_coeff(x, y):
    n = len(x)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_sqr = 0
    sum_y_sqr = 0
    for i, j in zip(x, y):
        sum_x += i
        sum_y += j
        sum_xy += i*j
        sum_x_sqr += i**2
        sum_y_sqr += j**2
    sample_x_mean = sum_x / n
    sample_y_mean = sum_y / n
    a1 = (n*sum_xy - sum_x * sum_y) / (n * sum_x_sqr - sum_x**2)
    a0 = sample_y_mean - a1 * sample_x_mean
    return a0, a1, sum_x, sum_y, sum_xy, sum_x_sqr, sum_y_sqr

def plot_linear_regression(x, y, a0, a1): 
    y_model = [a0 + a1 * i for i in x]
    plt.scatter(x, y)
    plt.plot(x, y_model)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Linear Regression - Least Squares')
    plt.show()

def least_squares(dataset): 
    x = dataset[0]
    y = dataset[1]
    n = len(x)
    a0, a1, sum_x, sum_y, sum_xy, sum_x_sqr, sum_y_sqr = compute_coeff(x, y)
    plot_linear_regression(x, y, a0, a1)
    n = len(x)
    r = (n * sum_xy - sum_x * sum_y) / (np.sqrt(n * sum_x_sqr - sum_x**2) * np.sqrt(n * sum_y_sqr - sum_y**2))
    return a0, a1, r**2, r

table_17_1 = [[1, 2, 3, 4, 5, 6, 7], #xi
              [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5], #yi
              [8.5765, 0.8622, 2.0408, 0.3265, 0.0051, 6.6122, 4.2908], #(yi - \bar{y})
              [0.1687, 0.5625, 0.3473, 0.3265, 0.5896, 0.7972, 0.1993]] #(yi - a0 - a1xi)^2

a0, a1, det_coeff, cor_coeff = least_squares(table_17_1)
print(a0, a1, det_coeff, cor_coeff)