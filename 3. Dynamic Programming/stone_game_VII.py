# def maxsum():
#     if isAlice:
#
#         alice1stOption = dp(left + 1, right, not isAlice) + getSum(left + 1, right)  # Take leftmost
#         alice2ndOption = dp(left, right - 1, not isAlice) + getSum(left, right - 1)  # Take rightmost
#         return max(alice1stOption, alice2ndOption)
#     else:
#         bobs1stOption = dp(left + 1, right, not isAlice) - getSum(left + 1, right)  # Take leftmost
#         bobs2ndOption = dp(left, right - 1, not isAlice) - getSum(left, right - 1)  # Take rightmost
#         return min(bobs1stOption, bobs2ndOption)


def stoneGameVII(stones):
        n = len(stones)
        pre = [0] * (n+1)
        for i in range(n):
            pre[i+1] = pre[i] + stones[i]

        def getSum(left, right):
            return pre[right+1] - pre[left]

        #@lru_cache(None)
        def dp(left, right, isAlice):
            if left > right: return 0

            if isAlice:
                a = dp(left+1, right, not isAlice) + getSum(left+1, right) # Take leftmost
                b = dp(left, right - 1, not isAlice) + getSum(left, right - 1) # Take rightmost
                return max(a, b)
            else:
                a = dp(left+1, right, not isAlice) - getSum(left+1, right) # Take leftmost
                b = dp(left, right - 1, not isAlice) - getSum(left, right - 1) # Take rightmost
                return min(a, b)

        return dp(0, n - 1, True)

if __name__=="__main__":
    ar = [5,3,1,4,2]
    print(stoneGameVII(ar))
