class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        is_negative = s[0] == '-'
        if is_negative:
            s = s[1:]
        reversed_s = s[::-1]
        reversed_int = int(reversed_s)
        if is_negative:
            reversed_int = -reversed_int
        # Check for 32-bit integer overflow
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int
