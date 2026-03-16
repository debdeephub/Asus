#A matrix is constructed of size n*n and given an integer ‘q’. The value at every cell of the matrix is given as, M(i,j) = i+j, where ‘M(i,j)' is the value of a cell, ‘i’ is the row number and ‘j’ is the column number. Return the number of cells having value ‘q’.

def query(n, q):
    # Write your code here
    # Return the number of cells having value ‘q’.
    c =  0
    matrix = [[0]*n for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = i+j+2
            if matrix[i][j]==q:
                c+=1
    return c
print(query(4,2)) #1
print(query(3,4)) #3
