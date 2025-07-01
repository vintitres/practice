class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        min_num = min(nums)
        nums = [num - min_num for num in nums]
        for i, num in enumerate(nums):
            num_bucket = num // (valueDiff + 1)
            if num_bucket in buckets:
                return True
            if num_bucket + 1 in buckets:
                if abs(num - buckets[num_bucket + 1]) <= valueDiff:
                    return True
            if num_bucket - 1 in buckets:
                if abs(num - buckets[num_bucket - 1]) <= valueDiff:
                    return True
            buckets[num_bucket] = num
            if i >= indexDiff:
                num_to_remove = nums[i - indexDiff]
                del buckets[num_to_remove // (valueDiff + 1)]
            i += 1
        return False
            
        
