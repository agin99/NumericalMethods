import numpy as np

def cholesky_decomp(M):
    L = [[0]*len(M[0]) for i in range(len(M))]
    for i in range(len(M)):
        for j in range(i+1):
            print(i, j)
            if i == j:
                L[i][j] = np.sqrt(M[i][j] - sum([k**2 for k in L[i][:j]]))
            else: 
                L[i][j] = (M[i][j] - sum([j*k for j, k in zip(L[i][:i],L[j][:i])])) / (L[j][j])
    return L
