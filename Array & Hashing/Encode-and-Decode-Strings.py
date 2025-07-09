class Solution:
    @staticmethod
    def encode(strs: list[str]) -> str:
        # Encode each string as length:string with # as separator
        return '#'.join(f'{len(s)}:{s}' for s in strs)
    
    @staticmethod
    def decode(s: str) -> list[str]:
        if not s:
            return []
        
        result = []
        i = 0
        while i < len(s):
            # Find colon to get length
            colon_idx = s.find(':', i)
            if colon_idx == -1:
                break
            # Extract length
            length = int(s[i:colon_idx])
            # Extract string of specified length
            result.append(s[colon_idx + 1:colon_idx + 1 + length])
            i = colon_idx + 1 + length + 1  # Move past string and # separator
        return result
