class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Char=set()
        max_length=0
        left=0

        for right in range(len(s)):
            if s[right] not in Char:
                Char.add(s[right])
                max_length = max(max_length,right-left+1)
            else:
                while s[right] in Char:
                    Char.remove(s[left])
                    left +=1
                Char.add(s[right])
        return max_length

    
        
        
