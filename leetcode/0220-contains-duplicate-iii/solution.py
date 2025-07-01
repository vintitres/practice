class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = defaultdict(Counter)
        min_num = min(nums)
        nums = [num - min_num for num in nums]
        for i, num in enumerate(nums):
            num_bucket = num // (valueDiff + 1)
            if num_bucket in buckets and len(buckets[num_bucket]):
                return True
            if num_bucket + 1 in buckets:
                for v in buckets[num_bucket + 1].keys():
                    if abs(num - v) <= valueDiff:
                        return True
            if num_bucket - 1 in buckets:
                for v in buckets[num_bucket - 1].keys():
                    if abs(num - v) <= valueDiff:
                        return True
            buckets[num_bucket].update([num])
            if i >= indexDiff:
                num_to_remove = nums[i - indexDiff]
                buckets[num_to_remove // (valueDiff + 1)][num_to_remove] -= 1
                if buckets[num_to_remove // (valueDiff + 1)][num_to_remove] == 0:
                    del buckets[num_to_remove // (valueDiff + 1)][num_to_remove]
            i += 1
        return False
            
        
