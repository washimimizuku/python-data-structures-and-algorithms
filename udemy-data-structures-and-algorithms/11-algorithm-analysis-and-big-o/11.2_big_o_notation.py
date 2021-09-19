import matplotlib.pyplot as plt
import numpy as np
from math import log


def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n + 1):
        final_sum += x

    return final_sum


def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n * (n + 1)) / 2


print(sum1(10))
print(sum2(10))


plt.style.use('bmh')

# Set up runtime comparisons
n = np.linspace(1, 10, 1000)
labels = ['Constant O(1)', 'Logarithmic O(log n)', 'Linear O(n)',
          'Log Linear O(n log n)', 'Quadratic O(n^2)', 'Cubic O(n^3)', 'Exponential O(2^n)']
big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n),
         n**2, n**3, 2**n]

# Plot setup
plt.figure(figsize=(12, 10))
plt.ylim(0, 50)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')

plt.show()
