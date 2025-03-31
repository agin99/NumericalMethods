
#Efficient
def evaluate_poly(poly, x):
    poly_sum = 0
    for index, i in enumerate(poly[len(poly)::-1]):
        poly_index = len(poly) - index - 1
        poly_sum = poly_sum * x + poly[poly_index]
    return poly_sum