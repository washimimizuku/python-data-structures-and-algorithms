'''
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using
the exact same letters (so you can just rearrange the
letters to get a different phrase or word).

For example:
    "public relations" is an anagram of "crap built on lies".
    "clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization
'''
from nose.tools import assert_equal


def anagram(s1, s2):
    s1_clean, s2_clean = [], []

    for letter in s1:
        if letter != ' ':
            s1_clean.append(letter)

    for letter in s2:
        if letter != ' ':
            s2_clean.append(letter)

    s1_clean.sort()
    s2_clean.sort()

    return s1_clean == s2_clean


assert(anagram('dog', 'god') == True)
assert(anagram('clint eastwood', 'old west action') == True)
assert(anagram('aa', 'bb') == False)

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


# Run Tests
t = AnagramTest()
t.test(anagram)
