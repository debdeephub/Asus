'''
    Time Complexity - O(4 ^ (N*M))
    Space Complexity - O(N*M)

    where N is the number of rows in the matrix
    and M is the number of columns in the matrix

'''
#from sys import stdin

INF = float("inf")


def backTrack(matrix, visited,
              i, j,  # Current cell
              x, y,  # Destination cell
              n, m): # Dimensions of matrix
    if (i < 0 or j < 0 or i >= n or j >= m):
        return INF

    if (matrix[i][j] == 0 or visited[i][j]):
        return INF

    #   If destination is found
    if (i == x and j == y):
            return 0

    visited[i][j] = 1

    moveLeft = backTrack(matrix, visited, i, j - 1, x, y, n, m)
    moveRight = backTrack(matrix, visited, i, j + 1, x, y, n, m)
    moveDRight = backTrack(matrix, visited, i+1, j + 1, x, y, n, m)
    moveUp = backTrack(matrix, visited, i - 1, j, x, y, n, m)
    moveDown = backTrack(matrix, visited, i + 1, j, x, y, n, m)

    visited[i][j] = 0

    #   Return the minimum path obtain from any direction
    return 1 + min(moveDown, moveUp, moveRight, moveLeft)


def findShortestPath(matrix, sourceX, sourceY, destX, destY, n, m):

    visited = [[False for i in range(m)] for j in range(n)]

    #   Backtrack from the source
    steps = backTrack(matrix, visited, sourceX, sourceY, destX, destY, n, m)

    if(steps >= INF):
        return -1

    return steps


#   taking input using fast I/O
def takeInput():
    n_x = input().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, input().strip().split(" "))) for row in range(n)]

    n_x = input().strip().split(" ")
    sourceX = int(n_x[0].strip())
    sourceY = int(n_x[1].strip())

    n_x = input().strip().split(" ")
    destX = int(n_x[0].strip())
    destY = int(n_x[1].strip())

    return matrix, sourceX, sourceY, destX, destY,  n, m


#   main
f=0
matrix, sourceX, sourceY, destX, destY,  n, m = takeInput()
f = findShortestPath(matrix, sourceX, sourceY, destX, destY,  n, m) if matrix[destX-1][destY-1]==0 else findShortestPath(matrix, sourceX, sourceY, destX, destY,  n, m)+1
print(f)
