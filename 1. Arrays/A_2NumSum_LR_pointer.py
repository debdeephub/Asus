class Solution:
    def twoNumSum(self,arr,num):
        #a = arr[:]
        #a = arr

        arr.sort()
        l = []
        left = 0
        right = len(arr)-1
        while left < right:
            total = arr[left]+arr[right]
            if total == num:
                l.append((arr[left],arr[right]))
                left+=1             #mistake
                right-=1            #mistake
            elif total > num:
                right-=1
            else:
                left+=1
        return l

#a = [3,5,-4,8,11,1,-1,6]
a = [3,5,4,-4,8,11,1,-1,6]
num = 10
print(Solution().twoNumSum(a,num))
