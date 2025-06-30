class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        mx = 0
        lengths = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        for i in reversed(range(len(nums1))):
            for j in reversed(range(len(nums2))):
                if nums1[i] == nums2[j]:
                    lengths[i][j] = 1 + (lengths[i + 1][j + 1] if i + 1 < len(nums1) and j + 1 < len(nums2) else 0)
                    mx = max(mx, lengths[i][j])
        return mx

