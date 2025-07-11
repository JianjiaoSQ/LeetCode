class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = ['']*2*n

        def dfs(left, right):
            if right == n:
                ans.append(''.join(path))
                return
            if left < n:
                path[left + right] = '('
                dfs(left+1, right)
            if left > right:
                path[left + right] = ')'
                dfs(left, right + 1)
        
        dfs(0, 0)
        return ans