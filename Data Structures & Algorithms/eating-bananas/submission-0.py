class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if self.calculate_hours(piles=piles, hours=mid) <= h: 
                ans = mid
                high = mid - 1
            else: low = mid + 1
        return ans
        
    def calculate_hours(self, piles: List[int], hours: int) -> int:
        totalHours = 0
        for banana in piles:
            totalHours += math.ceil(banana / hours)
        return totalHours