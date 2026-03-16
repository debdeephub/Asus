def saddlepoint(matrix):
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    lj = 0

    for i in range(r+1):
        lj = 0                        #mistake
        for j in range(1,c+1):
            if matrix[i][j] < matrix[i][lj]:
                lj = j
        flag = True
        for k in range(r+1):
            if matrix[i][lj] < matrix[k][lj]:
                flag = False
                break
        if flag :
            print(matrix[i][lj])


matrix = [[11,12,13,14],
          [21,22,23,34],
          [31,32,33,34],
          [41,42,43,44]]
saddlepoint(matrix)
