#[10, 20, 30, 40, 1, 2]
#91
class Solution:
    def fourSum(self,nums,target):
        nums.sort()
        l = []
        total = 0

        for i in range(len(nums)-3):
            left1 = i+1
            right1 = len(nums)-1
            while left1<right1:
                left2 = left1+1
                right2 = right1
                while left2<right2:
                    total = nums[i]+nums[left1]+nums[left2]+nums[right2]
                    if total == target:
                        l.append((nums[i],nums[left1],nums[left2],nums[right2]))
                        left2+=1
                        right2-=1
                    elif total > target:
                        right2-=1
                    else:
                        left2+=1
                left1+=1

        return l

a = [10, 20, 30, 40, 1, 2]
n = 33
print(Solution().fourSum(a,n))
