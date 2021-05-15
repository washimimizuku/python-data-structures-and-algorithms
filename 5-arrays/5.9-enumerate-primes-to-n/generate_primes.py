'''
Write a program that takes an integer argument and
retums all the primes between 1 and that integer.
For example, if the input is 18, you should return
[2, 3, 5, 7, 11, 13, 17].
'''


def generate_primes(n):  # Time: O(n log log n) | Space: O(n)
    primes = []

    # is_prime[p] represents if p is prime or not.
    # Initially, set each to true, except for 0 and 1.
    # Then use sieving to eliminate non-primes.
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            # Turn false all multiples of p.
            for i in range(p, n+1, p):
                is_prime[i] = False

    return primes


assert(generate_primes(18) == [2, 3, 5, 7, 11, 13, 17])


# Ignore even numbers and eliminate multiples of p2
# This will give better performance, but does not
# reflect on complexity
def generate_primes_square(n):  # Time: O(n log log n) | Space: O(n)
    if n < 2:
        return []

    primes = [2]  # Store the first prime number

    # is_prime[p] represents if (2i + 3) is prime or not.
    # Initially, set each to true.
    # Then use sieving to eliminate non-primes.
    size = (n - 3) // 2 + 1
    is_prime = [True] * size

    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)

            # Sieving fron p^2, where p^2 = (4i^2 + 12i + 9).
            # The index in is_prime is (2i^2 + 6i + 3) because
            # is_prime[i] represents 2i + 3.

            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes


assert(generate_primes_square(18) == [2, 3, 5, 7, 11, 13, 17])
