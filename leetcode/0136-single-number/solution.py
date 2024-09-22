class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorall = 0
        for num in nums:
            xorall ^= num
        return xorall
        
