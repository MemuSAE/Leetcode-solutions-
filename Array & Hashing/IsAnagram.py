class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return list(set(s))==list(set(t))
