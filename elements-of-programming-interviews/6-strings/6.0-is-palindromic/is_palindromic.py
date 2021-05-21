'''
A palindromic string is one which reads
the same when it is reversed.
'''


def is_palindromic(s):  # Time: O(n) | Space: O(1)
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    return all(s[i] == s[~i] for i in range(len(s) // 2))


assert(is_palindromic('abba') == True)
assert(is_palindromic('abcba') == True)
assert(is_palindromic('abcdef') == False)
