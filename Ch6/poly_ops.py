
def poly_mul(p1, p2):
    poly_result = []
    for index_i, i in enumerate(p1):
        for index_j, j in enumerate(p2):
            poly_result_index = index_i + index_j
            component_val = i * j
            if poly_result_index > len(poly_result) - 1: 
                poly_result.append(component_val)
            else: 
                poly_result[poly_result_index] += component_val
    return poly_result

def poly_div(p1, p2):
    poly_result = []
    for i in p1:
        poly_result.append(0)
    for index_i, i in enumerate(p1[::-1]):
        index_1 = len(p1) - index_i - 1
        index_2 = len(p2) - 1
        if len(p2) > len(p1) - index_i: 
            continue
        component_mul = p1[index_1]/p2[-1]
        for index_j in range(len(p2)):
            p1[index_1 - index_j] -= component_mul*p2[index_2 - index_j]
            poly_result[index_1 - index_2] = component_mul
    return poly_result, p1[:len(p2)]

def format_poly(poly):
    poly_string = []
    for index, i in enumerate(poly[::-1]):
        ind_true = len(poly) - index - 1
        abs_i = abs(i)
        symbol = ""
        if i > 0: 
            symbol = " + "
        elif i < 0:
            symbol = " - "
        else: 
            continue
        if ind_true == 0:
            poly_string.append(f"{symbol}{abs_i}")
        elif index == 0:
            poly_string.append(f"{abs_i}x^{ind_true}")
        else:
            poly_string.append(f"{symbol}{abs_i}x^{ind_true}")
    return poly_string