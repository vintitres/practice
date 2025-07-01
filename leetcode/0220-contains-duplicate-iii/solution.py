class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for i, num in enumerate(nums):
            # TODO find num in sorted ist woth bisect and see if neighbors close enough
            if window:
                j = window.bisect_right(num)
                if min(abs(window[j] - num) if j < len(window) else valueDiff + 1, abs(window[j - 1] - num) if j - 1 < len(window) else valueDiff + 1) <= valueDiff:
                    return True
            window.add(num)
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])
            i += 1
        return False
            
        
