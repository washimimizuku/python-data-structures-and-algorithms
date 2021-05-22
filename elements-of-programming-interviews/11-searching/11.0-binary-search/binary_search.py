'''
Binary search is a natural elimination-based
strategy for searching a sorted array.
'''
import bisect
import collections


def binary_seach(t, A):  # Time: O(log n)
    L, U = 0, len(A) - 1

    while L <= U:
        M = L + (U - L) // 2
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1

    return -1


assert(binary_seach(4, [1, 2, 3, 4, 5, 6]) == 3)


Student = collections.namedtuple('Student', ('name', 'grade_point_average'))


def comp_gpa(student):
    return (-student.grade_point_average, student.name)


def search_student(students, target, comp_gpa):  # Time: O(log n)
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target


students = []
students.append(Student('Julia', 9.9))
students.append(Student('Kevin', 8.2))
students.append(Student('Steve', 5.6))
students.append(Student('John', 5.6))
students.append(Student('Martin', 4.5))

assert(search_student(students, students[1], comp_gpa))
