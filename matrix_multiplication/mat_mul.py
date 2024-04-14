def matrix_multiply(matrix1, matrix2):
    k = len(matrix1)
    result = [[0 for _ in range(k)] for _ in range(k)]
    for i in range(k):
        for j in range(k):
            for l in range(k):
                result[i][j] = matrix1[i][l] * matrix2[l][j]

    return result


