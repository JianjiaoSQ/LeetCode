class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 使用的是回溯法
        if not digits:
            return []
        MAP = '', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
        path = [''] * len(digits)
        ans = []

        def dfs(i):
            if i == len(digits):
                ans.append(''.join(path))
                return
            for c in MAP[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        
        dfs(0)
        return ans