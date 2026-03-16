def stoneGame(stones):
    n = len(stones)
    g = 0
    dp = [[0 for _ in range(n)] for _ in range(n)]
    k = 0

    for g in range(0,len(stones)):
        for i,j in zip(range(0,len(stones)),range(g,len(stones))):

            if g == 0:
                dp[i][j] = stones[i]
            elif g == 1:
                dp[i][j] = max(stones[i],stones[j])
            else:
                val1 = stones[i] + min(dp[i+2][j],dp[i+1][j-1])
                val2 = stones[j] + min(dp[i+1][j-1],dp[i][j-2])
                val = max(val1,val2)
                dp[i][j] = val


    print(dp)



if __name__=="__main__":
    ar = [5,3,4,5]
    stoneGame(ar)
