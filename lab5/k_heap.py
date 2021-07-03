# @@file k_heap.py
# @author Hyosik Moon, Mingzhe Wang, Xing Li
# @date Feb. 21, 2021

import random


class KHeap:
    length = 0
    data = []
    k = None
    
    def __init__(self, values, k):
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap(values)
    
    # Note: Currently, the implementation of build_heap follows the fashion of build_heap1
    #       in heap.py.
    #       However, it may need to be modified if our testing results show build_heap2 or
    #       build_heap3 performs better than build_heap1.
    def build_heap(self, values):
        for i in range((self.length + self.k - 2)//self.k - 1, -1, -1):
            self.sink(i)
    
    def parent(self, i):
        return (i + self.k - 1) // self.k - 1
    
    def children(self, i):
        childs = []
        # _ = [1, 2, ..., k]
        for _ in range(1, self.k + 1):
            childs.append(i * self.k + _)
        return childs
    
    def sink(self, i):
        largest_known = i
        childs = self.children(i)
        for c in childs:
            if c < self.length and self.data[c] > self.data[largest_known]:
                largest_known = c
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)
            
    def __str__(self):
        s = ""
        i = 0
        while True:
            # included
            left_ind = (self.k**i - 1) // (self.k - 1)
            # excluded
            right_ind = (self.k**(i+1) - 1) // (self.k - 1)
            if right_ind > self.length:
                break
            for curr_ind in range(left_ind, right_ind):
                s += str(self.data[curr_ind]) + " "
                if curr_ind == right_ind - 1:
                    s += "\n"
            i += 1
        # print rest index
        curr_ind = left_ind
        while curr_ind < self.length:
            s += str(self.data[curr_ind]) + " "
            curr_ind += 1
        s += "\n"
        return s


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

########################## test for build_heap ###############################
L = create_random_list(25)
print("Original list:")
print(L)
print()
kheap = KHeap(L, 4)
print("Build result:")
print(kheap)
print("After k_heap list:")
print(L)


########################## test for build_heap ###############################
# L = [4,6,21,32,12,43,12,68,91,20,19,1,100,97,98,62,17]
# print(L)
# kheap = KHeap(L, 5)
# print(kheap)
