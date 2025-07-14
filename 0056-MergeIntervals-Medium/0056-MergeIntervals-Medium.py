class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newlist = intervals.sort(key=lambda x:x[0])
        ans = []

        for e in intervals:
            if not ans or ans[-1][1] < e[0]:
                ans.append(e)
            else:
                ans[-1][1] = max(ans[-1][1], e[1])
        
        return ans
        