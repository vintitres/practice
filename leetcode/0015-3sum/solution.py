class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # create a sorted copy
        triplets = []
        for i in range(0, len(nums)):
            n = nums[i]
            if i > 0 and nums[i - 1] == n:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                m = nums[j]
                o = nums[k]
                s = n + m + o
                if s > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]: 
                        k -= 1
                else:
                    if s == 0 and (not triplets or triplets[-1][1] != m or triplets[-1][2] != o):
                        triplets.append([n, m, o])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return triplets

        
