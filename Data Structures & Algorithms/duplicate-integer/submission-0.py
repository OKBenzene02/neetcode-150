from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = Counter(nums)
        for k, v in mp.items():
            if v >= 2: return True
        return False