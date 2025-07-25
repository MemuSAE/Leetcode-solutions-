class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        s = set(arr)
        dp = {}
        max_len = 0
        
        for j in range(1, n):
            for i in range(j):
                x = arr[i]
                y = arr[j]
                if y - x in s:
                    k = bisect.bisect_left(arr, y - x)
                    if k < i and arr[k] == y - x:
                        dp[(i, j)] = dp.get((k, i), 2) + 1
                        max_len = max(max_len, dp[(i, j)])
        
        return max_len if max_len >= 3 else 0
