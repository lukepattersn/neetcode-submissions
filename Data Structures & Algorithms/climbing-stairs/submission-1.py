class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * n
        print(dp)
        for i in range(1, n):
            dp[i] = dp[i - 1] + dp[i-2]
            print(dp[i])
        
        print(dp)
        return(dp[n-1])
        # dp[i] # number of ways to climb to top of stairs