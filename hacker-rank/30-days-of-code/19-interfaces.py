'''
https://www.hackerrank.com/challenges/30-interfaces

The AdvancedArithmetic interface and the method declaration for
the abstract divisorSum(n) method are provided for you in the
editor below.

Complete the implementation of Calculator class, which implements
the AdvancedArithmetic interface. The implementation for the
divisorSum(n) method must return the sum of all divisors of n.

Example:
n = 25
The divisors of 25 are 1, 5, 25. Their sum is 31.
'''


class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divsum = 0
        for i in range(n):
            if n % (i+1) == 0:
                divsum += i + 1
        return divsum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
