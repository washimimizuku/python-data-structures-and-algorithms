import random

'''
Implement a random number generator that generates a
random integer i between a and b, inclusive, given a
random number generator that produces zero or one with
equal probability? All values in [a,b] should be
equally likely.
'''


def uniform_random(lower_bound, upper_bound):  # O(log(b-a+1))
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | random.randint(0, 1)
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound


assert(uniform_random(0, 10)) <= 10
assert(uniform_random(10, 10)) == 10
assert(10 <= uniform_random(10, 20)) <= 20

for i in range(10):
    print(uniform_random(0, 10))
