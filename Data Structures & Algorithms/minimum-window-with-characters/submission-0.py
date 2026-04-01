class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = Counter(t)
        minLen, start, l = float('inf'), -1, 0
        count = 0

        for r in range(len(s)):
            if s[r] in mp:
                if mp[s[r]] > 0: count += 1
                mp[s[r]] -= 1
            
            while count == len(t):
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    start = l
                
                if s[l] in mp:
                    mp[s[l]] += 1
                    if mp[s[l]] > 0: count -= 1
                l += 1
        return "" if start == -1 else s[start: start + minLen]
            

