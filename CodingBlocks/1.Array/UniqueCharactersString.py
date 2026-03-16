n = input()
s = {'1'}
for i in range(int(n)):
    x = list(input())
    s.update(x)   
s.remove('1')
print(s)




