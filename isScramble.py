class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def check(s1: str, s2: str) -> bool:
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            if sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            n = len(s1)
            for i in range(1, n):
                if (check(s1[:i], s2[:i]) and check(s1[i:], s2[i:])) or \
                   (check(s1[:i], s2[n-i:]) and check(s1[i:], s2[:n-i])):
                    memo[(s1, s2)] = True
                    return True
            memo[(s1, s2)] = False
            return False
        return check(s1, s2)
