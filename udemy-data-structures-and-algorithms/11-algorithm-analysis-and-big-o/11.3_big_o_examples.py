def func_constant(values):  # Time: O(1) Constant
    print(values[0])


lst = [1, 2, 3]
func_constant(lst)


def func_linear(lst):  # Time: O(n) Linear
    for val in lst:
        print(val)


func_linear(lst)


def func_quadratic(lst):  # Time: O(n^2) Quadratic
    for item1 in lst:
        for item2 in lst:
            print(item1, item2)


func_quadratic(lst)


def print_once(lst):  # Time: O(n)
    for val in lst:
        print(val)


print_once(lst)


def print_twice(lst):  # Time: O(2n) -> O(n)
    for val in lst:
        print(val)

    for val in lst:
        print(val)


print_twice(lst)


def comp(lst):  # Time: O(1 + n/2 + 10) -> O/(n)
    print(lst[0])  # Time: O(1)

    midpoint = int(len(lst) / 2)

    for val in lst[:midpoint]:  # Time: O(n/2) -> O(n)
        print(val)

    for _ in range(10):  # Time: O(10)
        print('Hello World')


comp(lst)


def matcher(lst, match):  # Time: O(1) to O(n) -> O(n)
    for item in lst:
        if item == match:
            return True

    return False


matcher(lst, 1)  # Time: O(1)
matcher(lst, 11)  # Time: O(n)


def create_list(n):  # Time: O(n) | Space: O(n)
    new_list = []

    for _ in range(n):
        new_list.append('new')

    return new_list


print(create_list(10))


def printer(n):  # Time: O(n) | Space: O(1)
    for _ in range(n):
        print('Hello World!')


printer(10)
