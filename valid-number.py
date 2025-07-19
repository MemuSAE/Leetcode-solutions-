class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
            
        def isInteger(s, allowSign=True):
            if not s:
                return False
            if allowSign and s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()
            
        def isDecimal(s, allowSign=True):
            if not s:
                return False
            if allowSign and s[0] in ['+', '-']:
                s = s[1:]
            if s.startswith('.') and (len(s) == 1 or not s[1:].isdigit()):
                return False
            if s.endswith('.'):
                return s[:-1].isdigit()
            parts = s.split('.')
            if len(parts) != 2:
                return False
            left, right = parts
            return (not left or left.isdigit()) and right.isdigit()
            
        parts = s.lower().split('e')
        if len(parts) > 2:
            return False
            
        if len(parts) == 1:
            return isInteger(parts[0]) or isDecimal(parts[0])
            
        base, exp = parts
        return (isInteger(base, True) or isDecimal(base, True)) and isInteger(exp, True)
