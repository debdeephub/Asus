def maxprofit(arr,be,end,year):
    if be>end:
        return 0

    q1 = arr[be]*year + maxprofit(arr,be+1,end,year+1)
    q2 = arr[end]*year + maxprofit(arr,be,end-1,year+1)
    ans = max(q1,q2)
    return ans

# Driver code
if __name__=="__main__":
    ar = [1,4,2,3]
    print(maxprofit(ar,0,len(ar)-1,1))
