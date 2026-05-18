class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        slow1 = nums[0]
        while slow != slow1:
            slow = nums[slow]
            slow1 = nums[slow1]
        return slow