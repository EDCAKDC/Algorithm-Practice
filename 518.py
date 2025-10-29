class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            coin = coins[i-1]
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= coin:
                    dp[i][j] += dp[i][j-coin]
        return dp[n][amount]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount & 1 == 1 and all(coin==0 for coin in coins):
            return 0
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for target in range(coin,amount+1):
                dp[target] += dp[target-coin]
        return dp[amount]
        