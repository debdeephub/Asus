def Wave(matrix):
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    tot = (r+1)*(c+1)
    cnt = 0
    result = []
    while cnt < tot:
        for j in range(c+1):
            if j%2 == 0:
                for i in range(r+1):
                    result.append(matrix[i][j])
                    cnt+=1
            else:
                for i in reversed(range(r+1)):
                    result.append(matrix[i][j])
                    cnt+=1
    return result

matrix = [[ 1, 2, 3,],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ]]
print(Wave(matrix))
