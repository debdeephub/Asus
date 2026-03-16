l=[1,2,3,3,4,4,9,9,3,4,9]
left=0
right=len(l)-1
rflag,lflag=0,0
lresult,rresult=0,0
while left<right:
    if l[right]==4 and rflag!=1:
        rresult=right
        rflag=1
    elif l[left]==4 and lflag!=1:
        lresult=left
        lflag=1
    elif rflag==1:
         left+=1
    else:
        right-=1

print(lresult,rresult)