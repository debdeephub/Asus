def permutation(lst,n):


    if n == 0:
        return [[]]

    l = []

    for i in range(len(lst)):
       m = lst[i]

       remLst = lst[:i] + lst[i+1:]

       for p in permutation(remLst,n-1):
           l.append([m] + p)
    return l


# Driver code
if __name__=="__main__":
    arr ="12345"
    LL = permutation([x for x in arr], 2)
    print(LL)
