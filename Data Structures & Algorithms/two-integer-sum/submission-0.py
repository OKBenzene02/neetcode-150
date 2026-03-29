class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for r in range(len(nums)):
            right = target - nums[r]
            if right in mp: return [mp[right], r]
            mp[nums[r]] = r
        return [-1, -1]