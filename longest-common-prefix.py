class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        for i in range(len(prefix)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != prefix[i]:
                    return prefix[:i]
        return prefix
