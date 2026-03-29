class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf, pre = 1, 1
        res = [1] * n

        # Find the suffix 
        for i in range(n):
            res[i] *= suf
            suf *= nums[i]
        
        # find the prefix
        for i in range(n - 1, -1, -1):
            res[i] *= pre
            pre *= nums[i]

        return res