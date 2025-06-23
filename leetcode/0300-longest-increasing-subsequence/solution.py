class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def search(nums: int, n: int) -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = int((left + right) / 2)
                if nums[mid] >= n:
                    right = mid
                else:
                    left = mid + 1
            return left
                    
        longest = []
        for num in nums:
            if not longest or num > longest[-1]:
                longest.append(num)
            else:
                longest[search(longest, num)] = num
        return len(longest)

        
