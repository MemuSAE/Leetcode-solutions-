class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        remainders = [num % k for num in nums]
        max_length = 0
        
        for r in remainders:
            for c in range(k):
                dp[r][c] = dp[(c - r) % k][c] + 1
                if dp[r][c] > max_length:
                    max_length = dp[r][c]
        
        return max_length
