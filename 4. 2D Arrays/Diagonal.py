def diagonal(matrix):
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    result = [[] for i in range(c+1)]
    for i in range(r+1):
        for j  in range(c+1):
            diff = i - j
            if diff <=0:
                x = abs(diff)
                result[x].append(matrix[i][j])


    for i in result:
        #if i:
        for j in i:
            print(j,end =" ")

# matrix =[
#             [ 1, 2, 3, 4],
#             [ 4, 5, 6, 9 ],
#             [ 7, 8, 9, 11 ],
#         ]
matrix = [
            [ 1, 2, 3,],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ],
        ]

diagonal(matrix)
