'''
Implement a function that converts a spreadsheet column id
to the corresponding integer, with "A" corresponding to 1.
For example, you should return 4 for "D", 27 for "AN",
702 for "ZZ" , etc. 
'''
import functools


def ss_decode_col_id(col):  # Time: O(n)
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0
    )


assert(ss_decode_col_id('A') == 1)
assert(ss_decode_col_id('B') == 2)
assert(ss_decode_col_id('Y') == 25)
assert(ss_decode_col_id('Z') == 26)
assert(ss_decode_col_id('AA') == 27)
assert(ss_decode_col_id('AB') == 28)
assert(ss_decode_col_id('ZY') == 701)
assert(ss_decode_col_id('ZZ') == 702)
assert(ss_decode_col_id('M') == 13)
assert(ss_decode_col_id('BZ') == 78)
assert(ss_decode_col_id('CCC') == 2109)
