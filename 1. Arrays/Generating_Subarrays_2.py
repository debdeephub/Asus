l = [1,2,3]
l1 = []
result = []
for i in range(len(l)):
    for j in range(i,len(l)):
        for k in range(i,j+1):
            l1+= [l[k]]
        result.append(l1)
        l1 = []

print(result)
