class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:
                return dfs(i-1, c)
            return min(dfs(i-1, c), dfs(i, c-coins[i]) + 1)
         
        ans = dfs(len(coins)-1, amount)
        return ans if ans < inf else -1
        