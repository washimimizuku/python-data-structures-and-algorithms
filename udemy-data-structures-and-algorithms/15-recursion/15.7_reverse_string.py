'''
Reverse a string using recursion
'''


from nose.tools import assert_equal


def reverse(s):

    # Base case:
    if len(s) == 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]


class TestReverse(object):

    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')


# Run Tests
test = TestReverse()
test.test_rev(reverse)
