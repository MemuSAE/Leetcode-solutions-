from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count frequency of characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Decrement frequency for characters in t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        
        # If dictionary is empty, all characters matched
        return len(char_count) == 0
