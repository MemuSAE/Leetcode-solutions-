class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        
        # Calculate products of all elements to the left of each index
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        # Multiply by products of all elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
