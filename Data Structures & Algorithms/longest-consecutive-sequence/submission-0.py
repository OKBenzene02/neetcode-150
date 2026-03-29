class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxSeq = 0
        seq = 0
        for num in nums:
            if (num - 1) not in seen:
                seq = 0
                while (seq + num) in seen: seq += 1
            maxSeq = max(seq, maxSeq)
        return maxSeq
