def spiral(matrix,r,c):
    minr,minc = 0,0
    maxr,maxc =  r-1,c-1
    cnt = 0
    tne = r*c
    result = []
    while cnt<tne:

        #leftwall
        for i in range(minr,maxr+1,1):
            j = minc
            if cnt<tne:
                result.append(matrix[i][j])
                cnt+=1
        minc+=1
        #bottomwall
        for j in range(minc,maxc+1,1):
            i = maxr
            if cnt<tne:
                result.append(matrix[i][j])
                cnt+=1
        maxr-=1
        #rightwall
        for i in range(maxr,minr-1,-1):
            j = maxc
            if cnt<tne:
                result.append(matrix[i][j])
                cnt+=1
        maxc-=1
        #topwall
        for j in range(maxc,minc-1,-1):
            i = minr
            if cnt<tne:
                result.append(matrix[i][j])
                cnt+=1
        minr+=1
        
    print(result)
r,c = 3,3
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# matrix = [[1,20,19,18,17,16,15],
#           [2,21,31,30,29,14,0],
#           [3,22,32,33,34,13,0],
#           [4,23,24,25,26,27,12],
#           [5,6,7,8,9,10,11]]

spiral(matrix,r,c)
