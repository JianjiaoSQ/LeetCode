class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            ans = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, dfs(j))
            return ans + 1
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res
        