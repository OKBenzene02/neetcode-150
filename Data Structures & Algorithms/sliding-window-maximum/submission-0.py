class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # find the maximum at each window
        res = []
        queue = deque()
        for i in range(len(nums)):
            # check for indices that are not in the window
            while queue and queue[0] + k <= i: queue.popleft()

            # check for indices that are minimum and remove them
            while queue and nums[queue[-1]] < nums[i]: queue.pop()

            queue.append(i)
            if i >= k - 1: res.append(nums[queue[0]]) # maintain a window of size k
        return res