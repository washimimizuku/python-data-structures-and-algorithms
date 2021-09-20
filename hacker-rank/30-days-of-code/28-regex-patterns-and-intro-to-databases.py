'''
https://www.hackerrank.com/challenges/30-regex-patterns

Consider a database table, Emails, which has the attributes
First Name and Email ID. Given N rows of data simulating the
Emails table, print an alphabetically-ordered list of people
whose email address ends in @gmail.com.
'''

import re

if __name__ == '__main__':
    N = int(input())
    names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        regexp = re.compile(r'@gmail\.com')

        if regexp.search(emailID):
            names.append(firstName)

    names.sort()

    for name in names:
        print(name)
