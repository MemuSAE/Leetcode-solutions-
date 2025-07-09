class Solution:
    @staticmethod
    def encode(strs: list[str]) -> str:
        
        return '#'.join(f'{len(s)}:{s}' for s in strs)
    
    @staticmethod
    def decode(s: str) -> list[str]:
        if not s:
            return []
        
        result = []
        i = 0
        while i < len(s):
            
            colon_idx = s.find(':', i)
            if colon_idx == -1:
                break
            
            length = int(s[i:colon_idx])
            
            result.append(s[colon_idx + 1:colon_idx + 1 + length])
            i = colon_idx + 1 + length + 1 
        return result
