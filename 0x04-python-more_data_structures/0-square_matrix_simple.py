def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = list()
        for item in row:
            new_item = item * item
            new_row.append(new_item)
        new_matrix.append(new_row)
    return(new_matrix)
