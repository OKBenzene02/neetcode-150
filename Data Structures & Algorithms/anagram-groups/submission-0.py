class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for anagram in strs:
            mp[tuple(sorted(anagram))].append(anagram)
        return list(mp.values())

