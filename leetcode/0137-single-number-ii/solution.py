class Solution:
    BITS: int = 32
    def singleNumber(self, nums: List[int]) -> int:
        bit_count = [0] * Solution.BITS
        nums = [n + 2 ** (Solution.BITS - 1) for n in nums]
        for n in nums:
            i = 0
            while n > 0:
                bit_count[i] += n % 2
                i += 1
                n = int(n / 2)
        x = 0
        pow2 = 1
        for i in range(Solution.BITS):
            if bit_count[i] % 3 != 0:
                x += pow2
            pow2 *= 2
        return x - 2 ** (Solution.BITS - 1)



        
        
