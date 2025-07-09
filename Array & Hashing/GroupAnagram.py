class Solution:
    @staticmethod
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())
