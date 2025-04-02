from mat_ops import mat_flatten, mat_construct, dot_prod

def fwd_elim(m, b):
    m_flat = mat_flatten(m)
    for i in range(len(m) - 1):
        row_1 = m_flat[i*len(m[0]):(i+1)*len(m[0])]
        for j in range(i, len(m) - 1): 
            row_2 = m_flat[(j+1)*len(m[0]):(j+2)*len(m[0])]
            factor = row_2[i] / row_1[i]
            m_flat[(j+1)*len(m[0]):(j+2)*len(m[0])] = [l - k*factor for k, l in zip(row_1, row_2)]
            b[j+1] -= factor*b[i]
    return m_flat, b

def back_sub(upper_tri, b):
    x = [0]*len(b)
    for i in range(len(upper_tri), 0, -1):
        x[i-1] = (b[i-1] - dot_prod(x, upper_tri[i-1])) / upper_tri[i-1][i-1]
    return x

m = [[3, -0.1, -0.2],
       [0.1, 7, -0.3],
       [0.3, -0.2, 10]]
b = [7.85, -19.3, 71.4] 
upper_tri, b_tri = fwd_elim(m, b)
upper_tri = mat_construct(upper_tri, 3, 3)
x = back_sub(upper_tri, b_tri)
print(x)