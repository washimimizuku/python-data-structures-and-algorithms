'''
Write a program which takes an n x n 2D array and returns
the spiral ordering of the array.
'''


def matrix_in_spiral_order(square_matrix):  # Time: O(n2)
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix had odd dimention, and we are
            # at the center of the matrix square_matrix
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(list(zip(*square_matrix))
                               [-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(
            square_matrix[-1 - offset][-1 - offset:offset:-1])
        spiral_ordering.extend(list(zip(*square_matrix))
                               [offset][-1 - offset:offset:-1])

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)

    return spiral_ordering


matrix3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
matrix4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

assert(matrix_in_spiral_order(matrix3x3) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
assert(matrix_in_spiral_order(matrix4x4) == [
       1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])


def matrix_in_spiral_order_single(square_matrix):  # Time: O(n2) | Space: O(1)
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]

        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]

        x, y = next_x, next_y

    return spiral_ordering


assert(matrix_in_spiral_order_single(matrix3x3) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
assert(matrix_in_spiral_order_single(matrix4x4) == [
       1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
