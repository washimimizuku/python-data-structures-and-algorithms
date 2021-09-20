'''
https://www.hackerrank.com/challenges/30-nested-logic

Your local library needs your help! Given the expected and actual
return dates for a library book, create a program that calculates
the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date,
   no fine will be charged (i.e.: fine = 0).
2. If the book is returned after the expected return day but still
   within the same calendar month and year as the expected return
   date, fine = 15 Hackos x (the number of days late).
3. If the book is returned after the expected return month but still
   within the same calendar year as the expected return date, the
   fine = 500 Hackos x (the number of months late).
4. If the book is returned after the calendar year in which it was
   expected, there is a fixed fine of 10 000 Hackos.
'''

rDay, rMonth, rYear = [int(i) for i in input().split(' ')]
dDay, dMonth, dYear = [int(i) for i in input().split(' ')]

if dYear < rYear:
    print(10000)
elif dYear == rYear:
    if dMonth < rMonth:
        print((rMonth - dMonth) * 500)
    elif dDay < rDay:
        print((rDay - dDay) * 15)
    else:
        print(0)
else:
    print(0)
