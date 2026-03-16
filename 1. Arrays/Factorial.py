class Solution:
    f = 1
    def fact(self,n):
        #f = 1
        for i in range(2,n+1):
            self.f = self.f*i
        return self.f
n = int(input())
print(Solution().fact(n))
