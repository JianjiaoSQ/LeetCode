class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minprice = prices[0]

        for e in prices:
            ans = max(ans, e-minprice)
            minprice = min(minprice, e)
        return ans
        