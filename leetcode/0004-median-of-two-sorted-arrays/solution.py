class Solution:
    def count_nums_under(nums: List[int], x: int) -> int:
        b = 0
        e = len(nums)
        while b < e:
            m = (b + e) // 2
            if nums[m] < x:
                b = m + 1
            else:
                e = m
        return b
    
        
    def findNth(nums1: List[int], nums2: List[int], n: int) -> int:
        b = -10 ** 7
        e = 10 ** 7
        while b < e:
            m = (b + e) / 2 
            if Solution.count_nums_under(nums1, m) + Solution.count_nums_under(nums2, m) <= n:
                b = m
            else:
                e = m - 1
        pos1 = Solution.count_nums_under(nums1, b) 
        pos2 = Solution.count_nums_under(nums2, b)
        return min(nums1[pos1] if pos1 < len(nums1) else 10 ** 7, nums2[pos2] if pos2 < len(nums2) else 10 ** 7)



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) + len(nums2)) % 2 == 1:
            return Solution.findNth(nums1, nums2, (len(nums1) + len(nums2)) // 2)
        return (Solution.findNth(nums1, nums2, (len(nums1) + len(nums2) - 1) // 2) + Solution.findNth(nums1, nums2, (len(nums1) + len(nums2)) // 2)) / 2

        
        
