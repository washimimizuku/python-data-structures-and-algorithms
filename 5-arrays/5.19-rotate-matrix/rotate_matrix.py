'''
Write a function that takes as input an
n x n 2D array, and rotates the array by 
90 degrees clockwise.
'''


def rotate_matrix(square_matrix):  # Time: O(n2) | Space: O(1)
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange.
            # Note that A[-i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
            (
                square_matrix[i][j],
                square_matrix[-j][i],
                square_matrix[-i][-j],
                square_matrix[j][-i]
            ) = (
                square_matrix[-j][i],
                square_matrix[-i][-j],
                square_matrix[j][-i],
                square_matrix[i][j]
            )

    return square_matrix


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(rotate_matrix(matrix))
# NOT WORKING!!!
# Should be [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]


class RotateMatrix:
    def __init__(self, square_matrix):
        self._square_matrix = square_matrix

    def read_emtry(self, i, j):
        # Note that A[-i] for i in [0, len(A) - 1] is A[-(i + 1)].
        return self._square_matrix[-j][i]

    def write_entry(self, i, j, v):
        self._square_matrix[-j][i] = v


matrix_obj = RotateMatrix(matrix)
print(matrix_obj.read_emtry(0, 0))
print(matrix_obj.read_emtry(3, 3))
