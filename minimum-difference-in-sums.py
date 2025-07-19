class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_sum = sum(nums)
        left = []
        right = []
        heapq.heapify(left)
        heapq.heapify(right)
        sum_left = 0
        for i in range(n):
            sum_left += nums[i]
            heapq.heappush(left, -nums[i])
        min_left = [0] * (n + 1)
        min_left[0] = sum_left
        for i in range(n, 2 * n):
            heapq.heappush(left, -nums[i])
            sum_left += nums[i]
            sum_left += heapq.heappop(left)
            min_left[i - n + 1] = sum_left
        sum_right = 0
        for i in range(2 * n, 3 * n):
            sum_right += nums[i]
            heapq.heappush(right, nums[i])
        max_right = [0] * (n + 1)
        max_right[n] = sum_right
        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(right, nums[i])
            sum_right += nums[i]
            sum_right -= heapq.heappop(right)
            max_right[i - n] = sum_right
        result = float('inf')
        for i in range(n + 1):
            result = min(result, min_left[i] - max_right[i])
        return result
