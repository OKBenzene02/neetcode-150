class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        l, r = 0, m
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = (m + n + 1) // 2 - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r1 = float('inf') if mid1 == m else nums1[mid1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0: return (max(l1, l2) + min(r1, r2)) / 2
                else: return max(l1, l2)
            
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1