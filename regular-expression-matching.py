class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        processed = []
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == '*':
                processed.append((p[i], '*'))
                i += 2
            else:
                processed.append((p[i], ''))
                i += 1

        memo = {}

        def dfs(i: int, j: int) -> bool:
            if j >= len(processed):
                return i >= len(s)
            if i > len(s):
                return False\

            if (i, j) in memo:
                return memo[(i, j)]
                
            char, star = processed[j]
            match = i < len(s) and (char == '.' or s[i] == char)
            if star == '*':
                result = dfs(i, j + 1) or (match and dfs(i + 1, j))
            else:
                result = match and dfs(i + 1, j + 1)
            memo[(i, j)] = result
            return result
        return dfs(0, 0)
