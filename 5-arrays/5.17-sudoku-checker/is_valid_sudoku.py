'''
Check whether a 9x9 2D arcay representing a partially
completed Sudoku is valid.
Specifically, check that no row, column, or 3 x 3 2D
subarray contains duplicates.
A O-value in the 2D array indicates that entry is blank;
every other entry is in [1,9].
'''
import collections
import math


# Check if a partially filled matrix has any conflics
def is_valid_sudoku(matrix):  # Time: O(n2) | Space: O(n)
    # Returm True if subarray
    # partial_assignnent[start_row:end_row][start_col:end_col]
    # contains any dupTicates in [1, 2, ..., len(partial_assignnent)];
    # otherwise return False.
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(matrix)
    # Check row and column constraints.
    if any(has_duplicate([matrix[i][j] for j in range(n)])
            or has_duplicate([matrix[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([matrix[a][b]
                                  for a in range(region_size * I, region_size * (I+1))
                                  for b in range(region_size * J, region_size * (J+1))])
               for I in range(region_size) for J in range(region_size))


sudoku_partial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

sudoku_complete = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
sudoku_invalid = [
    [3, 5, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

assert(is_valid_sudoku(sudoku_partial))
assert(is_valid_sudoku(sudoku_complete))
assert(is_valid_sudoku(sudoku_invalid) == False)


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(matrix):  # Time: O(n2) | Space: O(n)
    region_size = int(math.sqrt(len(matrix)))
    return max(
        collections.Counter(k
                            for i, row in enumerate(matrix)
                            for j, c in enumerate(row)
                            if c != 0
                            for k in ((i, str(c)), (str(c), j),
                                      (i / region_size, j/region_size,
                                       str(c)))).values(),
        default=0) <= 1


assert(is_valid_sudoku_pythonic(sudoku_partial))
assert(is_valid_sudoku_pythonic(sudoku_complete))
assert(is_valid_sudoku_pythonic(sudoku_invalid) == False)
