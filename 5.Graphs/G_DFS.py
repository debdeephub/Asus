matrix = [[0,1,1,0],
          [0,0,1,0],
          [1,0,0,1],
          [0,0,0,1]]

visited = [0,0,0,0]

stack = [0]
visited[0] = 1

node = stack.pop(len(stack)-1)
print(node)

while True:
    for x in range(0,len(visited)):
        if matrix[node][x] == 1 and  visited[x] == 0:
            visited[x] = 1
            stack.append(x)
    if len(stack) == 0:
        break;
    node = stack.pop(len(stack)-1)
    print(node)
