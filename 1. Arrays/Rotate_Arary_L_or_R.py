rowL  = [1,3,5,7,9,11]
rowR = [1,3,5,7,9,11]
k = 2
#row[0: k] = row[0: k][:-1] #ommi last character
rowL[0: k] = rowL[0: k][: :-1]
rowL[k: ] = rowL[k: ][: : -1]
rowL[:] = rowL[:][: : -1]
#row[:] = row[:][: : -1]
rowR = rowR[-k:] + rowR[:-k]
print(rowL)
print(rowR)
