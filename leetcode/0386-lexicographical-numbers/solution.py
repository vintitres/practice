class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(self.fn(n))

    def fn(self, n: int):
        yield 1
        num = 10
        while num > 1:
            if num <= n:
                yield num
                num *= 10
            else:
                num = int(num / 10)
                while num % 10 == 9: 
                    num = int(num / 10)
                num += 1
        
