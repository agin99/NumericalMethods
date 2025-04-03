
def dot_prod(v1, v2): 
    return sum([i*j for i, j in zip(v1, v2)])

def gauss_seidel(M, B, e_s):
    e_a = [1 for i in range(len(e_s))]
    x = [B[0], 0, 0]
    D = [i[index] for index, i in enumerate(M)]
    while True:
        for j in range(len(x)):
            prev_x = x[j]
            x[j] = -B[j] 
            x_dot = [-1*k for k in x]
            M[j][j] = 1
            x[j] = dot_prod(x_dot, M[j])/D[j]
            e_a[j] = abs((x[j] - prev_x)/x[j])
        within_desired_error = False
        for i in range(len(e_a)):
            if e_a[i] <= e_s[i]: 
                within_desired_error = True
        if within_desired_error:
            break
    return x, e_a