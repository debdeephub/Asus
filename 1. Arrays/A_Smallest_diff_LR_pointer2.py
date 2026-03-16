aOne = [-1,5,10,20,28,3]
aTwo = [26,134,135,15,17]
m = float('inf')
l = {(i,j):abs(i-j) for i in aOne for j in aTwo}
for k,v in l.items():
    if v < m:
        m = v
        r = k

print(r,m)
