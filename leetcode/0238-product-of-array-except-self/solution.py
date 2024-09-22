class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productR = [None] * len(nums)
        product = 1
        for i, n in enumerate(reversed(nums)):
            product *= n
            productR[len(nums) - 1 - i] = product
        def get(product, index):
            return product[index] if index >= 0 and index < len(product) else 1
        product = 1
        ret = [None] * len(nums)
        for i, num in enumerate(nums):
            ret[i] = product * get(productR, i + 1)
            product *= num
        return ret
