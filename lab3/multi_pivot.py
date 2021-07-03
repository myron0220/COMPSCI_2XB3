#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@brief This module experiments with multiple pivots in quick sort
@author Xing Li
"""

################
# Orignal Code #
################
import random


def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

############
# New Code #
############


#@@ brief This function recursively run quicksort with multiple pivots
#@  param L The list to be sorted
#@  param n The number of pivots
#@  return partially sorted array with multiple pivots
def quicksort_copy(L,n):
    if len(L) < 2:
        return L
    pivot_num = min(n, len(L)-1) # Adjust when the length is too short
    pivots = quicksort_copy(L[0:pivot_num], 1) # Set up a list of pivots
    containers = [[] for _ in range(pivot_num)] # Set up a list of containers for between pivots
    containers.append([]) # The number of containers is always one more than the number of pivots
    for num in L[pivot_num:]: # For all elements other than pivots
        for i in range(pivot_num): # Compare an element with each pivot and put in one container
            if num < pivots[i]:
                containers[i].append(num)
                break
        if num >= pivots[pivot_num - 1]:
            containers[pivot_num].append(num)
    result = []
    for i in range(pivot_num): #concatenate the elements in each container as well as pivots
        result += quicksort_copy(containers[i],n) + [pivots[i]]
    return result + quicksort_copy(containers[pivot_num],n)

def dual_pivot_quicksort(L):
    copy = quicksort_copy(L, 2)
    for i in range(len(L)):
        L[i] = copy[i]
    return L

def tri_pivot_quicksort(L):
    copy = quicksort_copy(L, 3)
    for i in range(len(L)):
        L[i] = copy[i]
    return L

def quad_pivot_quicksort(L):
    copy = quicksort_copy(L, 4)
    for i in range(len(L)):
        L[i] = copy[i]
    return L

def one_pivot_quicksort(L):
    copy = quicksort_copy(L, 1)
    for i in range(len(L)):
        L[i] = copy[i]
    return L

# test
L = [6, 3, 10, 8, 0]
print("Before:\n")
print(L)
dual_pivot_quicksort(L)
print("After:\n")
print(L)
L = [6,3,10,8,0]
print("Before:\n")
print(L)
tri_pivot_quicksort(L)
print("After:\n")
print(L)
L = [6,3,10,8,0]
print("Before:\n")
print(L)
quad_pivot_quicksort(L)
print("After:\n")
print(L)


# Check sorting algorithms
for _ in range(10):
    L = create_random_list(10)
    print("1", L, one_pivot_quicksort(L.copy()))
    print("2", L, dual_pivot_quicksort(L.copy()))
    print("3", L, tri_pivot_quicksort(L.copy()))
    print("4", L, quad_pivot_quicksort(L.copy()))
    print()