class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
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
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        return False
            
        
