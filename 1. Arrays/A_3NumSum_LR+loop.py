class Solution:
    def threeNumSum(self,arr,target):
        triplets = []
        left = 0
        right = len(arr)-1
        arr.sort()
        for i in range(0,len(arr)-2):   #mistake
            left = i+1                  #mistake
            right = len(arr)-1          #mistake
            while left < right:
                total = arr[i]+arr[left]+arr[right]
                if total == target:
                    triplets.append((arr[i],arr[left],arr[right]))
                    left+=1
                    right-=1
                elif total > target:
                    right-=1
                else:
                    left+=1
        return triplets

a = [12,3,1,2,-6,5,-8,6]
n = 0
print(Solution().threeNumSum(a,n))
