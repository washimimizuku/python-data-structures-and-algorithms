import collections
import functools

'''
Design a hash function suitable for strings.
'''


def string_hash(s, modulus):  # Time: O(1)
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)


assert(string_hash('something', 2) == 0)


'''
Write a program that takes as input a set of words and
retums groups of anagrams for those words. Each group
must contain at least two words.
'''


def find_anagrams(dictionary):  # Time: O(nm log n)
    sorted_string_to_anagram = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends
        # the original string as another value into hash table.
        sorted_string_to_anagram[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagram.values() if len(group) >= 2
    ]


dictionary = ["debitcard", "elvis", "silent", "badcredit",
              "lives", "freedom", "listen", "levis", "money"]
expected_result = [['debitcard', 'badcredit'], [
    'elvis', 'lives', 'levis'], ['silent', 'listen']]
assert(find_anagrams(dictionary) == expected_result)


'''
Consider a class that represents contacts. For simplicity,
assume each contact is a string. Suppose it is a hard requirement
that the individual contacts are to be stored in a list and it's
possible that the list contains duplicates.
'''


class ContactList:
    def __init__(self, names):
        # names is a list of strings
        self.names = names

    def __hash__(self):
        # Conceptually we want to hash the set of name.
        # Since the set type is mutable, it cannot be hashed.
        # Therefore we use frozenset.
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)


def merge_contact_lists(contacts):
    # contacts is a list of ContactList.
    return list(set(contacts))


contacts1 = ContactList(['John', 'Steve', 'Amanda'])
contacts2 = ContactList(['Jasmine', 'Steve', 'Paula'])

assert(len(merge_contact_lists([contacts1, contacts2])) == 2)
