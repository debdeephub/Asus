class Solution:
    def twoNumSum(self,arr,num):
        h = {}
        l = []
        for i in arr:
            match = num - i
            if match in h:
                l.append((match,i))
            else:
                h[i] = True
        return l

#a = [3,5,-4,8,11,1,-1,6]
a = [3,5,4,-4,8,11,1,-1,6]
num = 10
print(Solution().twoNumSum(a,num))
