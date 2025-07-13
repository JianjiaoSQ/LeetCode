class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            res = max(dfs(i-1), dfs(i-2)+nums[i])
            return res
        return dfs(n-1)


        