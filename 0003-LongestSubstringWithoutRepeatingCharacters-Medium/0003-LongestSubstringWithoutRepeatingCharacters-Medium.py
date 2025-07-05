class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, ans = 0, 0
        win = set()
        for index, value in enumerate(s):
            while value in win:
                win.remove(s[left])
                left += 1
            win.add(value)
            ans = max(ans, index-left+1)
        return ans
        