def check_top(matrix, m, k):
    for i in range(0, m):
        for j in range(len(matrix[i])):
            if j==k and matrix[i][j] == 0:
                return 0
    return 1

def solution(matrix):
    
    r = sum(matrix[0])
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if i>0 and check_top(matrix, i, j):
                r += matrix[i][j]
    return r
