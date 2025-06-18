class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        ln = len(nums)
        resln = int(ln / 3)
        res = [0] * resln
        while i < resln:
            ii = i * 3
            if nums[ii + 2] > nums[ii] + k:
                return []
            res[i] = [nums[ii], nums[ii + 1], nums[ii + 2]]
            i += 1
        return res
        
