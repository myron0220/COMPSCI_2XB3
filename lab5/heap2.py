# @@file heap.py
# @author Hyosik Moon, Mingzhe Wang, Xing Li
# @date Feb. 21, 2021

import math


class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap3()

    def build_heap1(self):
        # Client in __init__ (plz replace all codes in __init__ with the below codes!):
        ######################################################################
        # self.data = L
        # self.length = len(L)
        # self.build_heap1()
        ######################################################################
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def build_heap2(self, L):
        # Client in __init__ (plz replace all codes in __init__ with the below codes!):
        ######################################################################
        # self.data = []
        # self.length = 0
        # self.build_heap2(L)
        ######################################################################
        self.insert_values(L)

    def build_heap3(self):
        # Client in __init__ (plz replace all codes in __init__ with the below codes!):
        ######################################################################
        # self.data = L
        # self.length = len(L)
        # self.build_heap3()
        ######################################################################
        while True:
            # for test for this process
            # print(self)
            for i in range(self.length):
                self.sink(i)
            if self.is_heap():
                break
        
    def is_heap(self):
        # for all internal (non-leaf) nodes
        # i = [0, 1, 2, ..., self.length // 2 - 1]
        for i in range(self.length // 2):
            # if right child is inside the bound, the left child must be inside the bound,
            # then no need to check for the left child.
            if self.right(i) < self.length:
                if self.data[self.left(i)] > self.data[i]:
                    return False
                if self.data[self.right(i)] > self.data[i]:
                    return False
            # if right child is outside the bound, then need to check for the left child.
            # however, because the current node is an internal one, the left child must 
            # inside the bound. (no need to check)
            else:
                if self.data[self.left(i)] > self.data[i]:
                    return False
        return True
    
    def sink(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.sink(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

########################### test for build_heap ##############################
L = [5,12,3,7,31,2,100,99]
heap = Heap(L)
print("Build result: ")
print(heap)

############################ test for is_heap ################################
# L = [5,12,3,7,31,2,100,99]
# heap = Heap(L)
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# heap = Heap(L)
# heap.data[5] = 6
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# heap = Heap(L)
# heap.data[5] = 5
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# heap = Heap(L)
# heap.data[4] = 100
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# heap = Heap(L)
# heap.data[4] = 99
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# heap = Heap(L)
# heap.data[7] = 100
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# heap = Heap(L)
# heap.data[7] = 12
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
# L = [100,100,100,100,100,100]
# heap = Heap(L)
# print(heap)
# print("is_heap: ", heap.is_heap())
# print()
