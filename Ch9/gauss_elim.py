from mat_ops import mat_flatten, dot_prod

def fwd_elim(m, b):
    m_flat = mat_flatten(m)
    for i in range(len(m) - 1):
        row_1 = m_flat[i*len(m[0]):(i+1)*len(m[0])]
        for row_ind in range(i, len(m) - 1):
            if row_1[i] == 0:
                if m_flat[(i+row_ind)*len(m[0]):(i+1+row_ind)*len(m[0])][i] != 0:
                    temp_b = b[i]
                    b[i] = b[i+row_ind]
                    b[i+row_ind] = temp_b
                    temp_row = row_1
                    m_flat[i*len(m[0]):(i+1)*len(m[0])] = m_flat[(i+row_ind)*len(m[0]):(i+1+row_ind)*len(m[0])]
                    m_flat[(i+row_ind)*len(m[0]):(i+1+row_ind)*len(m[0])] = temp_row
                    row_1 = m_flat[i*len(m[0]):(i+1)*len(m[0])]
            row_2 = m_flat[(row_ind+1)*len(m[0]):(row_ind+2)*len(m[0])]
            factor = row_2[i] / row_1[i]
            m_flat[(row_ind+1)*len(m[0]):(row_ind+2)*len(m[0])] = [l - k*factor for k, l in zip(row_1, row_2)]
            b[row_ind+1] -= factor*b[i]
    return m_flat, b

def back_sub(upper_tri, b):
    x = [0]*len(b)
    for i in range(len(upper_tri), 0, -1):
        x[i-1] = (b[i-1] - dot_prod(x, upper_tri[i-1])) / upper_tri[i-1][i-1]
    return x