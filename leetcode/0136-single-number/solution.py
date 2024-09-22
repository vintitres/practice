import itertools
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return list(itertools.accumulate(nums, xor))[-1]
