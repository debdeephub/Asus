class Solution:
	def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
		end = len(nums) - k
		ans = []
		for num in nums:
			while end and ans and num < ans[-1] :
				ans.pop()
				end -= 1
			ans.append(num)

		return ans[:k]


class Solution1:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            while stack and len(stack)+len(nums)-i>k and stack[-1] > nums[i]:
                stack.pop()
            stack.append(nums[i])
        return stack[:k]
