class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # simple logic calculate the pse and nse
        n = len(heights)
        nse, pse = [0] * n, [0] * n
        maxArea = 0

        # calculate the pse
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]: stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # calculate the nse
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]: stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        
        # calculate the area
        for i in range(n):
            maxArea = max(maxArea, heights[i] * (nse[i] - pse[i] - 1))
        return maxArea
