class StockSpanner:
    price_history: List[int]
    skip: List[int]

    def __init__(self):
        self.price_history = []
        self.skip = []
        

    def next(self, price: int) -> int:
        length = 1
        i = len(self.price_history) - 1
        while i >= 0:
            if self.price_history[i] <= price:
                length += self.skip[i]
                i -= self.skip[i]
            else:
                break
        self.skip.append(length)
        self.price_history.append(price)
        return length
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
