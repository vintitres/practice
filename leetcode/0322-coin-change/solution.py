class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

           0 0 0 0 0 0 0 0 0
        1: 1 2 3 4 5 6 7 8 9
        2: 1 2 1 2 1 2 1 2 1


        """
        min_coins = [0] + [-1] * (amount)
        for coin in coins:
            for i in range(amount + 1 - coin):
                c = min_coins[i]
                if c == -1:
                    continue
                if min_coins[i + coin] == -1:
                    min_coins[i + coin] = c + 1
                else:
                    min_coins[i + coin] = min(c + 1, min_coins[i + coin])
        return min_coins[amount]
        
