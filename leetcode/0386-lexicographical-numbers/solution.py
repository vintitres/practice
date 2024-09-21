class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        nums = []
        while len(nums) < n:
            if num <= n:
                nums.append(num)
                num *= 10
            else:
                num = int(num / 10)
                while num % 10 == 9: 
                    num = int(num / 10)
                else:
                    num += 1
        return nums
        
