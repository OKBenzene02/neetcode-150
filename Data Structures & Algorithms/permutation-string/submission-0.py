class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = Counter(s1)
        window = dict()
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if (r - l + 1) > len(s1):
                window[s2[l]] = window.get(s2[l], 0) - 1
                if window[s2[l]] == 0: del window[s2[l]]
                l += 1
            if mp == window: return True
        return False