class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        log = nums1 + nums2
        log = sorted(log)

        n=len(log)
        if n%2 ==1:
            return log[n//2]
        else:
            return (log[(n // 2) - 1] + log[n // 2]) / 2
        

        
