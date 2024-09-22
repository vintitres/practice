import functools
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(xor, nums)
