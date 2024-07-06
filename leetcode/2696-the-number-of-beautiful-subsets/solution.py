class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        x = 0
        for i in range(1, 1<<len(nums)):
            s = set()
            ok = True
            for j in range(0, len(nums)):
                if 1<<j & i:
                    if nums[j] + k in s or nums[j] - k in s:
                        ok = False
                        break
                    s.add(nums[j])
            if ok:
                x += 1
        return x
