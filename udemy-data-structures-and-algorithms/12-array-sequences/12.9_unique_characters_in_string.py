'''
Given a string, determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should
return True. The string 'aabcde' contains duplicate characters and
should return false.
'''

from nose.tools import assert_equal


def uni_char(s):
    return len(set(s)) == len(s)


def uni_char2(s):

    characters = set()

    for letter in s:
        # Check if in set
        if letter in characters:
            return False
        else:
            # Add it to the set
            characters.add(letter)

    return True


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestUnique()
t.test(uni_char)
t.test(uni_char2)
