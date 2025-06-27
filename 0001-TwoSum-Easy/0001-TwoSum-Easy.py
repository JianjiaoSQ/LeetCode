class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for index, value in enumerate(nums):
            if target-value in table:
                return [index, table[target-value]]
            else:
                table[value] = index
        return []  