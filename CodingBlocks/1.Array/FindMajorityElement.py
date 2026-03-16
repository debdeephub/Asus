n = input().strip()
ele = input().strip().split(" ")

dict = {}

for i in ele:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for k,v in dict.items():
    if v > (int(n)//3):
        print(k,end=" ")

