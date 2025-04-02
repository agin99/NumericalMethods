
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

def mat_add(m1, m2): 
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError(f"Incorrect dimensions for addition: \n{len(m1)}x{len(m1[0])}, {len(m2)}x{len(m2[0])}")
    m1_flat = mat_flatten(m1)
    m2_flat = mat_flatten(m2)
    return mat_construct([i + j for i, j in zip(m1_flat, m2_flat)], len(m1), len(m1[0]))

def mat_sub(m1, m2): 
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError(f"Incorrect dimensions for subtraction: \n{len(m1)}x{len(m1[0])}, {len(m2)}x{len(m2[0])}")
    m1_flat = mat_flatten(m1)
    m2_flat = mat_flatten(m2)
    return mat_construct([i - j for i, j in zip(m1_flat, m2_flat)], len(m1), len(m1[0]))

def mat_mul(m1, m2): 
    prod = []
    if len(m1[0]) != len(m2):
        raise ValueError(f"Incorrect dimensions for multiplication: \n{len(m1)}x{len(m1[0])}, {len(m2)}x{len(m2[0])}")
    m1_flat = mat_flatten(m1)
    m2_flat = mat_flatten(m2)
    for index in range(len(m1) * len(m2[0])):
        row = m1_flat[(index//2)*len(m1[0]):(index//2 + 1)*len(m1[0])]
        col = [m2_flat[index % len(m1) + j*len(m1)] for j in range(len(m2))]
        prod.append(dot_prod(row, col))
    return prod

def mat_t(m):
    rows = len(m)
    cols = len(m[0])
    m_t = [[0]*rows for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            m_t[j][i] = m[i][j]  
    return m_t

def mat_det_2d(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def mat_det(m):
    coeff = m[0]
    if len(m) == 2:
        return mat_det_2d(m)
    m_d = m[1:]
    det = 0
    for index, i in enumerate(coeff):
        mat_minor = [i[:index]+i[index+1:] for i in m_d]
        if len(mat_minor) > 2:
            det_mat_minor = mat_det(mat_minor)
        else: 
            det_mat_minor = mat_det_2d(mat_minor)
        det += (-1)**(index)*coeff[index]*det_mat_minor
    return det

def mat_inv():
    pass

mat1 = [[1, 0, 1], 
        [0, 1, 0]]
mat2 = [[2, 1], 
        [1, 2],
        [1, 1]]
mat_prod_1_2 = mat_mul(mat1, mat2)
mat3 = [[0.3, 0.52, 1, 1],
        [0.5, 1, 1.9, 1],
        [0.1, 0.3, 0.5, 1],
        [1, 1, 1, 1]]
mat_det_3 = mat_det(mat3)
mat_1_t = mat_t(mat1)
mat_2_t = mat_t(mat2)
