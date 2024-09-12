class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        last_start = nums[0]
        last = nums[0]
        output = []
        for num in nums[1:] + [nums[-1] + 2]:
            if last + 1 == num:
                last += 1
            else:
                output.append(f"{last_start}->{last}" if last_start != last else f"{last}")
                last = num
                last_start = num
        return output

        
