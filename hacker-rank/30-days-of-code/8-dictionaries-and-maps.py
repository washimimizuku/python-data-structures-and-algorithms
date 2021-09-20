'''
https://www.hackerrank.com/challenges/30-dictionaries-and-maps
'''

phoneBook = {}
n = int(input())

for i in range(0, n):
    text = input()
    splittedText = text.split()
    phoneBook[splittedText[0]] = splittedText[1]

while True:
    try:
        text = input()
    except:
        break

    if text in phoneBook:
        print(text + '=' + phoneBook[text])
    else:
        print('Not found')
