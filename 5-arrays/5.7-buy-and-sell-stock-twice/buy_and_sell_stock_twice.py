'''
Write a program that computes the maximum profit that
can be made by buying and selling a share at most twice.
The second buy must be made on another date after the
first sale.
'''


def buy_and_sell_stock_twice(prices):  # Time: O(n) | Space: O(n)
    min_price_so_far = float('inf')  # Infinite value
    max_total_profit = 0.0
    first_buy_sell_profits = [0] * len(prices)

    # Forward phase. For each day, we record maximum
    # profit if we sell on that day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum
    # profit if we nake the second buy on that day.
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i - 1])

    return max_total_profit


assert(buy_and_sell_stock_twice([12, 11, 13, 9, 12, 8, 14, 13, 15]) == 10)
assert(buy_and_sell_stock_twice(
    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 55)
