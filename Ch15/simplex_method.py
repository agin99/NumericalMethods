import math

def set_slack_variables(M, Z): 
    for i in range(len(M)):
        M[i] = M[i] + [0]*i + [1] + [0]*(len(M) - i - 1)
    Z = [-i for i in Z]
    return Z + [0]*len(M), M

def find_entering(Z_slack):
    max_value = 0 
    entering_index = 0
    for index, i in enumerate(Z_slack):
        if i < max_value:
            max_value = i
            entering_index = index
    return entering_index, max_value

def find_leaving(M_slack, entering_index, solution_set):
    min_intercept = math.inf
    leaving_index = None
    for index, i in enumerate(solution_set):
        if M_slack[index][entering_index] <= 0: 
            continue
        if i / M_slack[index][entering_index] < min_intercept:
            min_intercept = i / M_slack[index][entering_index]
            leaving_index = index
    return leaving_index, min_intercept

def update_system(B_Z, B, Z_slack, M_slack, entering_index, leaving_index):
    denom = M_slack[leaving_index][entering_index]
    M_slack[leaving_index] = [i / denom for i in M_slack[leaving_index]]
    B[leaving_index] /= denom
    factor_z = Z_slack[entering_index] / denom
    Z_slack = [i - Z_slack[entering_index] / denom*j for i, j in zip(Z_slack, M_slack[leaving_index])]
    B_Z -= factor_z * B[leaving_index]
    for i in range(len(M_slack)):
        factor = M_slack[i][entering_index] / denom
        if i == leaving_index: 
            continue
        M_slack[i] = [j - factor*k for j, k in zip(M_slack[i], M_slack[leaving_index])]
        B[i] -= factor*B[leaving_index]
    return B_Z, B, Z_slack, M_slack

def simplex_algorithm(M, B, Z, B_Z):
    var_labels = [f"x{i}" for i in range(len(Z))]
    Z_slack, M_slack = set_slack_variables(M, Z)
    var_labels += [f"S{i}" for i in range(len(Z_slack[len(Z):]))]
    final_labels = [f"S{i}" for i in range(len(Z_slack[len(Z):]))]
    prev_optim = 0
    while True: 
        entering_index, _ = find_entering(Z_slack)
        leaving_index, _ = find_leaving(M_slack, entering_index, B)
        final_labels[leaving_index] = var_labels[entering_index]
        B_Z, B, Z_slack, M_slack = update_system(B_Z, B, Z_slack, M_slack, entering_index, leaving_index)
        if prev_optim > B_Z * 0.99:
            return B_Z, B, final_labels
        prev_optim = B_Z

def sort_solution(final_labels, B):
    new_B = []
    for index, i in enumerate(final_labels):
        if 'x' in i: 
            new_B.append(B[index])
    return new_B

M = [[7, 11],
     [10, 8],
     [1, 0],
     [0, 1]]
B = [77, 80, 9, 6]
Z = [150, 175]
B_Z = 0

B_Z, B, final_labels = simplex_algorithm(M, B, Z, B_Z)
print(f"Optimal Z = {B_Z}")
print(f"X Vals: {sort_solution(final_labels, B)}")