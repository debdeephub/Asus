def exit(matrix):
    r = len(matrix)
    c = len(matrix[0])
    i,j, dir = 0,0,0
    while(True):
        dir = (dir+matrix[i][j])%4
        if dir == 0:
            j+=1
        elif dir == 1:
            i+=1
        elif dir == 2:
            j-=1
        elif dir == 3:
            i-=1

        if i<0:
            i+=1
            break
        elif j<0:
            j+=1
            break
        elif i>r-1:
            i-=1
            break
        elif j>c-1:
            j-=1
            break
    print(i,j)

matrix = [[0,0,1,0],
          [1,0,0,1],
          [0,0,0,1],
          [1,0,1,0]]
exit(matrix)
