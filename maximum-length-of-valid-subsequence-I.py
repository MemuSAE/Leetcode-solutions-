class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        even_count = sum(1 for num in nums if num % 2 == 0)
        odd_count = len(nums) - even_count
        
        dp = [[0] * 2 for _ in range(2)]
        
        
        for num in nums:
            parity = num % 2
            
            dp[0][parity] = dp[1][1 - parity] + 1  
            dp[1][parity] = dp[0][1 - parity] + 1  
        
        return max(even_count, odd_count, dp[0][0], dp[0][1], dp[1][0], dp[1][1])
