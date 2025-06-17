class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # create a sorted copy
        triplets = []
        last = nums[0] + 1
        for i in range(0, len(nums)):
            n = nums[i]
            if last == n:
                continue
            else:
                last = n
            j = i + 1
            k = len(nums) - 1
            while j < k:
                m = nums[j]
                o = nums[k]
                s = n + m + o
                if s == 0:
                    if len(triplets) == 0 or triplets[-1][1] != m or triplets[-1][2] != o:
                        triplets.append([n, m, o])
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return triplets

        
