class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(arr, temp, res, target, ind):
            if ind == len(arr):
                if target == 0: res.append(list(temp))
                return
            
            if arr[ind] <= target:
                temp.append(arr[ind])
                solve(arr, temp, res, target - arr[ind], ind)
                temp.pop()
            solve(arr, temp, res, target, ind + 1)

        solve(nums, [], res, target, 0)

        return res