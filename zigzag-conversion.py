class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        result = []
        cycle = 2 * numRows - 2
        for row in range(numRows):
            for i in range(row, len(s), cycle):
                result.append(s[i])
                if row > 0 and row < numRows - 1 and i + cycle - 2 * row < len(s):
                    result.append(s[i + cycle - 2 * row])
        return ''.join(result)
