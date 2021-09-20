'''
Given a string of words, reverse all the words. For example:

Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
'''

from nose.tools import assert_equal


def rev_word(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:

                # Get index where word ends
                i += 1

            # Append that word to the list
            words.append(s[word_start:i])

        # Add to index
        i += 1

    """
    Reverse words.
    """

    reversed_words = []
    index_words = len(words) - 1

    while index_words >= 0:
        reversed_words.append(words[index_words])
        index_words -= 1

    return " ".join(reversed_words)


def rev_word1(s):
    return " ".join(reversed(s.split()))


def rev_word2(s):
    return " ".join(s.split()[::-1])


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '),
                     'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word)
t.test(rev_word1)
t.test(rev_word2)
