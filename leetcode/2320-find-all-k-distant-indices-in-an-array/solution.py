class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        i = 0
        j = 0
        ret = []
        for j, num in enumerate(nums):
            if num == key:
                i = max(i, j - k)
                while i < len(nums) and i <= j + k:
                    ret.append(i)
                    i += 1
        return ret

        
