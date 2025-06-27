class Solution:
    def climbStairs(self, n: int) -> int:
        # 为了减少重复计算 使用缓存装饰器
        @cache
        def dfs(i):
            if i <= 1:
                return 1
            return dfs(i-1) + dfs(i-2)
        return dfs(n)
        