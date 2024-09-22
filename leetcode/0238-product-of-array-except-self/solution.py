class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productR = []
        product = 1
        for n in reversed(nums):
            product *= n
            productR.append(product)
        productR.reverse()
        def get(product, index):
            return product[index] if index >= 0 and index < len(product) else 1
        product = 1
        ret = []
        for i, num in enumerate(nums):
            ret.append(product * get(productR, i + 1))
            product *= num
        return ret
