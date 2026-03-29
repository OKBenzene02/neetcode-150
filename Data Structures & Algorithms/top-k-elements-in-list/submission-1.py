class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)

        reverseSortMap = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i, v in reverseSortMap:
            res.append(i)
            if len(res) == k: return res