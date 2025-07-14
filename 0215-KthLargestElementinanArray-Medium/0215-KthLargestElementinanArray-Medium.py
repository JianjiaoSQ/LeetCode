class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(nums, k):
            n = random.choice(nums)
            big, eq, small = [], [], []

            for num in nums:
                if num > n:
                    big.append(num)
                elif num < n:
                    small.append(num)
                else:
                    eq.append(num)
            
            if k <= len(big):
                return quick(big, k)
            if len(nums) - len(small) < k:
                return quick(small, k-len(nums)+len(small))
            return n
        
        return quick(nums, k)
        