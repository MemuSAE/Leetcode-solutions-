class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        m = 10001
        last = [-1]*m
        l = 0
        s = 0
        best = 0
        for r, v in enumerate(nums):
            if last[v] >= l:
                while l <= last[v]:
                    s -= nums[l]
                    l += 1
            last[v] = r
            s += v
            if s > best:
                best = s
        return best
