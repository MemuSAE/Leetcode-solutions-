class Solution:
    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        # Count frequency of each number
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Create buckets where index represents frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Collect top k frequent elements from buckets
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    return result[:k]
        
        return result[:k]
