'''
For US currency, wherein coins take values 
1, 5, 10, 25, 50, 100 cents, the greedy algorithm
for making change results in the minimum number of coins.
'''


def change_making(cents):  # Time: O(1)
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0

    for coin in COINS:
        num_coins += cents // coin
        cents %= coin

    return num_coins


assert(change_making(555) == 7)
