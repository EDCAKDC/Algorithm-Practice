class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold = - prices[0]
        sold = 0
        rest = 0

        for p in prices[1:]:
            pre_hold, pre_sold, pre_rest = hold, sold, rest

            hold = max(pre_hold, pre_rest - p)
            sold = pre_hold + p
            rest = max(pre_rest, pre_sold)
        return max(rest, sold)