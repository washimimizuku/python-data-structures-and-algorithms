'''
 Write a program that takes an array denoting the daily
 stock price, and retums the maximum profit that could
 be made by buying and then selling one share of that stock.
 There is no need to buy if no profit is possible.
'''


def buy_and_sell_stock_once(prices):  # Time: O(n) | Space: O(1)
    min_price_so_far = float('inf')  # Infinite value
    max_profit = 0.0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(price, min_price_so_far)

    return max_profit


assert(buy_and_sell_stock_once([40, 20, 30]) == 10)
assert(buy_and_sell_stock_once(
    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30)
