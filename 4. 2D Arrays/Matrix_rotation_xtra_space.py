def mrotation(matrix):
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    result = [[0 for i in range(r+1)] for j in range(c+1)]
    for i in range(r+1):
        for j in range(c+1):
            result[j][c-i] = matrix[i][j]
    print(result)





matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
mrotation(matrix)
