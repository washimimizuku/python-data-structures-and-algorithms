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


def anagram(s1, s2):  # My solution
    s1_clean, s2_clean = [], []

    for letter in s1:
        if letter != ' ':
            s1_clean.append(letter.lower())

    for letter in s2:
        if letter != ' ':
            s2_clean.append(letter.lower())

    s1_clean.sort()
    s2_clean.sort()

    return s1_clean == s2_clean


def anagram2(s1, s2):  # Example solution 1
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


def anagram3(s1, s2):  # Example solution 2
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case check
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        assert_equal(sol('dog', 'god'), True)
        assert_equal(sol('clint eastwood', 'Old West action'), True)
        assert_equal(sol('public relations', 'crap built on lies'), True)
        assert_equal(sol('aa', 'bb'), False)
        assert_equal(sol('aaa', 'AAA'), True)
        print("ALL TEST CASES PASSED")


# Run Tests
t = AnagramTest()
t.test(anagram)
t.test(anagram2)
t.test(anagram3)
