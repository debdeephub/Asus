class Solution:
    def Move(self, arr, ele):
        i = 0
        j = len(arr)-1
        while i<j:
            while i<j and arr[j] == ele:     #mistake
                j-=1
            if arr[i] == ele:
                arr[i],arr[j] = arr[j],arr[i]
            i+=1
        return arr

arr = [4,1,2,2,2,3,2,2]
ele = 2
print(Solution().Move(arr,ele))
