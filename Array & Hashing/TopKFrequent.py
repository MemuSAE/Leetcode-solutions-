class Solution:
    @staticmethod
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    return result[:k]
        
        return result[:k]
