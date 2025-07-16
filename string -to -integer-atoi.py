class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] in {'-', '+'}:
            sign = -1 if s[0] == '-' else 1
            i += 1
        result = 0
        digits = set('0123456789')
        while i < len(s) and s[i] in digits:
            result = result * 10 + int(s[i])
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31
            i += 1
        return result * sign
