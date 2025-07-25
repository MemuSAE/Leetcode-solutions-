class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = cur_max = cur_min = 0
        for num in nums:
            cur_max = max(num, cur_max + num)
            cur_min = min(num, cur_min + num)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        return max(max_sum, -min_sum)
