class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        count = 0
        while i <= j:
            while j > i and nums[i] + nums[j] > target:
                j -= 1
            if nums[i] + nums[j] > target:
                break
            count += pow(2, j - i, MOD) 
            count %= MOD
            print(i, j, count)
            i += 1
        return count
        
