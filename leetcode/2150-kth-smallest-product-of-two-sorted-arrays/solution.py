class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_up_to(x: int):
            count = 0
            for num1 in nums1:
                if num1 > 0:
                    count += bisect_right(nums2, x // num1)
                elif num1 < 0:
                    count += len(nums2) - bisect_left(nums2, ceil(x / num1))
                else:
                    if x >= 0:
                        count += len(nums2)
            return count
        left = - 10 ** 10 - 1
        right = 10 ** 10 + 1
        while left < right:
            print(left, right)
            mid = (left + right + 1) // 2
            if count_up_to(mid) >= k:
                right = mid - 1
            else:
                left = mid
        return left + 1





        
