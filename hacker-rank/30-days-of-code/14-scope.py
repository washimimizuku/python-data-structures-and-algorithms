'''
https://www.hackerrank.com/challenges/30-scope

Complete the Difference class by writing the following:
1. A class constructor that takes an array of integers as a parameter and saves
   it to the __elements instance variable.
2. A computeDifference method that finds the maximum absolute difference between
   any 2 numbers in __elements and stores it in the maximumDifference instance variable.
'''


class Difference:
    maximumDifference = 0

    def __init__(self, a):
        self.__elements = a

    def __init__(self, elements):
        self.__elements = elements

    def computeDifference(self):
        for element in self.__elements:
            for element2 in self.__elements:
                difference = abs(element - element2)
                if (difference > self.maximumDifference):
                    self.maximumDifference = difference


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
