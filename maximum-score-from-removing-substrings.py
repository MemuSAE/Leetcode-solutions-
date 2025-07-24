class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, pair: str, points: int) -> tuple[int, str]:
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == pair[0] and c == pair[1]:
                    stack.pop()
                    score += points
                else:
                    stack.append(c)
            return score, ''.join(stack)
        
        total_score = 0
        if x >= y:
            score_ab, new_s = remove_pair(s, "ab", x)
            score_ba, _ = remove_pair(new_s, "ba", y)
            total_score = score_ab + score_ba
        else:
            score_ba, new_s = remove_pair(s, "ba", y)
            score_ab, _ = remove_pair(new_s, "ab", x)
            total_score = score_ba + score_ab
            
        return total_score
