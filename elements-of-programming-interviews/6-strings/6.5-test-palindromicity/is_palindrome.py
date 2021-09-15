'''
Implement a function which takes as input a string s
and returns true if s is a palindromic string.
'''


def is_palindrome(s):  # Time: O(n)
    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1
    while i < j:
        # i and j both skip non-alphanumeric characters.
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i, j = i + 1, j - 1

    return True


assert(is_palindrome('A man, a plan, a canal, Panama.') == True)
assert(is_palindrome('Able was I, ere I saw Elba!') == True)
assert(is_palindrome('Ray a Ray') == False)
