class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = dict()
        l = 0
        maxLen, maxFreq = 0, 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            maxFreq = max(maxFreq, mp[s[r]])
            if (r - l + 1) - maxFreq > k:
                mp[s[l]] = mp.get(s[l], 0) - 1
                if mp[s[l]] == 0: mp.pop(s[l])
                l += 1
            else:
                maxLen = max(maxLen, r - l + 1)
        return maxLen