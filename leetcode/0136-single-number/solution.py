import itertools
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        *_, last = itertools.accumulate(nums, lambda a,b: a^b)
        return last
