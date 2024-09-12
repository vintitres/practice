class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = m + n - 1
        while i >= 0:
            nums1[j] = nums1[i]
            i -= 1
            j -= 1
        i = n
        j = 0
        k = 0
        while k < n + m:
            if j == n or (i < m + n and nums1[i] < nums2[j]):
                nums1[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1
            
             
        
