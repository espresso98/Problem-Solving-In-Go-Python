# Find the maximum profit you can achieve with cooldown one day 
# you must sell the stock before you buy again
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# A: cooldown, B: held, C: sold

# O(N), O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = sold = -math.inf # held: buy, hold the maxprofit, sold: sell the stock
        cooldown = 0  # the starting point or sell the previous day and rest
        for price in prices:
            held, sold, cooldown = max(held, cooldown - price), held + price, max(cooldown, sold)
        return max(sold, cooldown)
