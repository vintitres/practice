class Solution:
    def can(self, nums: List[int], p: int, mx: int) -> bool:
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= mx:
                p -= 1
                if (p == 0):
                    return True
                i += 2
            else:
                i += 1
        return False
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums: List[int] = sorted(nums)
        b = 0
        e = nums[-1] - nums[0]
        #print(nums)
        while b < e:
            m = int((b + e) / 2)
            #print(b, e, m)
            if self.can(nums, p, m):
                #print("can")
                e = m
            else:
                #print("can't")
                b = m + 1
        return b


