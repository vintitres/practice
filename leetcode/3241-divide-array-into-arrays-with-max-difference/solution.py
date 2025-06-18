class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []
        ln = len(nums)
        print(nums)
        while i < ln:
            if nums[i + 2] > nums[i] + k:
                return []
            res += [[nums[i], nums[i + 1], nums[i + 2]]]
            i += 3
        return res
        
