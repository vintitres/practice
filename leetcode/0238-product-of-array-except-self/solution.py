class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productL = []
        productR = []
        product = 1
        for n in nums:
            product *= n
            productL.append(product)
        product = 1
        for n in reversed(nums):
            product *= n
            productR.append(product)
        productR.reverse()
        def get(product, index):
            return product[index] if index >= 0 and index < len(product) else 1

        return [get(productL, i - 1) * get(productR, i + 1)
            for i in range(len(nums))]
        
