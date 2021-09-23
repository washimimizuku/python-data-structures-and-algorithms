'''
Binary Heap

The basic operations we will implement for our binary heap are as follows:
1. BinaryHeap() creates a new, empty, binary heap.
2. insert(k) adds a new item to the heap.
3. findMin() returns the item with the minimum key value, leaving item in the heap.
4. delMin() returns the item with the minimum key value, removing the item from the heap.
5. isEmpty() returns true if the heap is empty, false otherwise.
6. size() returns the number of items in the heap.
7. buildHeap(list) builds a new heap from a list of keys.
'''


class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):

        while i // 2 > 0:

            if self.heap_list[i] < self.heap_list[i // 2]:

                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp

            i = i // 2

    def insert(self, k):

        self.heap_list.append[k]
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, i):

        while (i * 2) <= self.current_size:

            mc = self.min_child(i)

            if self.heap_list[i] > self.heap_list[mc]:

                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp

            i = mc

    def min_child(self, i):

        if i * 2 + 1 > self.current_size:

            return i * 2

        else:

            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):

        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)

        return retval

    def build_heap(self, alist):

        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]

        while (i > 0):
            self.perc_down(i)
            i = i - 1


bh = BinaryHeap()
bh.build_heap([9, 6, 5, 2, 3])
print(bh.heap_list)
