class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxCapacity = 0
        while l < r:
            maxCapacity = max((r - l) * min(heights[l], heights[r]), maxCapacity)
            if heights[l] > heights[r]: r -= 1
            else: l += 1
        return maxCapacity