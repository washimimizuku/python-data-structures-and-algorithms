#!/bin/python3

'''
https://www.hackerrank.com/challenges/30-operators
'''


def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost + meal_cost * tip_percent/100 + meal_cost * tax_percent/100
    print(round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
