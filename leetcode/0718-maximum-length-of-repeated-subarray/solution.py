class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        mx = 0
        last_lengths = [0 for _ in range(len(nums2))]
        for i in reversed(range(len(nums1))):
            lengths = [0 for _ in range(len(nums2))]
            for j in reversed(range(len(nums2))):
                if nums1[i] == nums2[j]:
                    lengths[j] = 1 + (last_lengths[j + 1] if j + 1 < len(nums2) else 0)
                    mx = max(mx, lengths[j])
            last_lengths = lengths
        return mx

