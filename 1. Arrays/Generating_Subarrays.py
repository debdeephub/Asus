l = [1,2,3]
result = [ l[i:j+1] for i in range(len(l)) for j in range(i,len(l)) ]
result.sort(key=len)
print(result)
