'''
https://www.hackerrank.com/challenges/30-dictionaries-and-maps

Given n names and phone numbers, assemble a phone book that maps friends'
names to their respective phone numbers. You will then be given an unknown
number of names to query your phone book for. For each name queried, print
the associated entry from your phone book on a new line in the form "name=phoneNumber";
if an entry for name is not found, print "Not found" instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
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
