
class Solution:
    def maxOperations(self,nums,k):
        ans = 0
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 0
        for n in nums:
            if (k - n) in freq.keys() and freq[k - n] > 0:
                #dict.has_key(key)
                #key in dict
                freq[k - n] -= 1
                ans += 1
            else:
                freq[n] += 1
        return ans

nums = [3,1,3,4,3]
k = 6
print(Solution().maxOperations(nums,k))






# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
