class StockSpanner:
    price_history: List[int]

    def __init__(self):
        self.price_history = []
        

    def next(self, price: int) -> int:
        length = 1
        for ph in reversed(self.price_history):
            if ph <= price:
                length += 1
            else:
                break
        self.price_history.append(price)
        return length
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
