class Solution:
    def isMonotonicInc(self,arr):
        a = arr[:]
        start = 0
        def Inc(a,start):
            if start == len(a)-1:
                return True
            if a[start] > a[start+1] or a[start] == a[start+1] :   #mistake
                return False
            else:
                return Inc(a,start+1)
        return Inc(a,start)
    def isMonotonicDec(self,arr):
        a = arr[:]
        start = 0
        def Dec(a,start):
            if start == len(a)-1:
                return True
            if a[start] < a[start+1] or a[start] == a[start+1]:
                return False
            else:
                return Dec(a,start+1)
        return Dec(a,start)

#arr = [1,2,3,5,4,5,6,7]
arr = [1,2,3,4,4,5,6,7]
print(Solution().isMonotonicInc(arr))
print(Solution().isMonotonicDec(arr))
