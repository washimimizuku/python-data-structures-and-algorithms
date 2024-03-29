import ctypes


class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds!')

        return self.A[k]  # Retrieve from array at index k

    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # Double capacity if not enough room

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()


# Instantiate
arr = DynamicArray()

# Append new element
arr.append(1)
# Check length
print(len(arr))

# Append new element
arr.append(2)
# Check length
print(len(arr))

# index
print(arr[0])
print(arr[1])

# Check Size
# Set n
n = 10

for i in range(n):

    # Number of elements
    a = len(arr)

    # Actual size in bytes
    b = arr.capacity

    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a, b))

    # increase length by one
    arr.append(n)
