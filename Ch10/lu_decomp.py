
def dot_prod(v1, v2): 
    return sum([i*j for i, j in zip(v1, v2)])

def mat_flatten(m): 
    m_flat = []
    for index_row, row in enumerate(m): 
        for index_col, col in enumerate(row): 
            m_flat.append(m[index_row][index_col])
    return m_flat

def mat_construct(m_flat, rows, cols): 
    m = []
    for i in range(rows):
        m.append([])
        for j in range(cols): 
            m[-1].append(0)
    for index, i in enumerate(m_flat):
        m[index // cols][index % cols] = i
    return m

def mat_t(m):
    rows = len(m)
    cols = len(m[0])
    m_t = [[0]*rows for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            m_t[j][i] = m[i][j]  
    return m_t

def lu_decomp(m):
    rows = len(m)
    cols = len(m[0])
    m_flat = mat_flatten(m)
    lower_tri = [0 for i in range(len(m_flat))]
    for i in range(len(m) - 1):
        row_1 = m_flat[i*len(m[0]):(i+1)*len(m[0])]
        lower_tri_row = lower_tri[i*len(m[0]):(i+1)*len(m[0])]
        for row_ind in range(i, len(m) - 1):
            if row_1[i] == 0:
                for row_ind_partial_pivot in range(i, len(m) - 1):
                    if m_flat[(i+row_ind_partial_pivot)*len(m[0]):(i+1+row_ind_partial_pivot)*len(m[0])][i] != 0:
                        temp_lower_tri = lower_tri_row
                        lower_tri[i*len(m[0]):(i+1)*len(m[0])] = lower_tri[(i+row_ind_partial_pivot)*len(m[0]):(i+1+row_ind_partial_pivot)*len(m[0])]
                        lower_tri[(i+row_ind_partial_pivot)*len(m[0]):(i+1+row_ind_partial_pivot)*len(m[0])] = temp_lower_tri
                        temp_row = row_1
                        m_flat[i*len(m[0]):(i+1)*len(m[0])] = m_flat[(i+row_ind_partial_pivot)*len(m[0]):(i+1+row_ind_partial_pivot)*len(m[0])]
                        m_flat[(i+row_ind_partial_pivot)*len(m[0]):(i+1+row_ind_partial_pivot)*len(m[0])] = temp_row
                        row_1 = m_flat[i*len(m[0]):(i+1)*len(m[0])]
            row_2 = m_flat[(row_ind+1)*len(m[0]):(row_ind+2)*len(m[0])]
            factor = row_2[i] / row_1[i]
            lower_tri[(row_ind+1)*len(m[0]) + i] = factor
            m_flat[(row_ind+1)*len(m[0]):(row_ind+2)*len(m[0])] = [l - k*factor for k, l in zip(row_1, row_2)]
    l_tri_constr = mat_construct(lower_tri, rows, cols)
    for i in range(len(l_tri_constr)):
        l_tri_constr[i][i] = 1
    lower_tri = mat_flatten(l_tri_constr)
    return m_flat, lower_tri

def fwd_sub(l_tri, b):
    x = [0]*len(b)
    for i in range(len(l_tri)):
        x[i] = (b[i] - dot_prod(x, l_tri[i])) / l_tri[i][i]
    return x

def back_sub(u_tri, y):
    x = [0]*len(b)
    for i in range(len(u_tri), 0, -1):
        x[i-1] = (y[i-1] - dot_prod(x, u_tri[i-1])) / u_tri[i-1][i-1]
    return x

def mat_inverse(l_tri, u_tri):
    inv = []
    for i in range(len(l_tri)):
        b = [0 for i in range(len(l_tri))]
        b[i] = 1
        print(b)
        y = fwd_sub(l_tri, b)
        x = back_sub(u_tri, y)
        inv.append(x)
    inv = mat_t(inv)
    return inv

m = [[3, -0.1, -0.2],
     [0.1, 7, -0.3],
     [0.3, -0.2, 10]]
b = [7.85, -19.3, 71.4]

u_tri, l_tri = lu_decomp(m)
u_tri_constr = mat_construct(u_tri, len(m), len(m[0]))
l_tri_constr = mat_construct(l_tri, len(m), len(m[0]))
m_inv = mat_inverse(l_tri_constr, u_tri_constr)
