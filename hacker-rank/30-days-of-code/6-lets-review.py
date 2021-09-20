'''
https://www.hackerrank.com/challenges/30-review-loop
'''

numberOfTimes = int(input())

if numberOfTimes >= 1 and numberOfTimes <= 10:

    for j in range(0, numberOfTimes):
        text = input()

        a = ''
        b = ''

        if len(text) >= 2 and len(text) <= 10000:
            for i in range(0, len(text)):
                if i % 2:
                    a = a + text[i]
                else:
                    b = b + text[i]

            print(b, a)
