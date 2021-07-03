import random
import math
import timeit
from lab3 import create_random_list


def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
    return L


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
        L.append(random.randint(1, n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    if factor == 0:
        return L
    for _ in range(math.ceil(n * factor)):
        index1 = random.randint(0, n - 1)
        index2 = random.randint(0, n - 1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


####################


def bubblesort(L):  # Avg, Worst case bubblesort
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1):
            if (L[j] > L[j + 1]):
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


def bubblesort_opt(L):  # Avg, Worst case bubblesort
    n = len(L)
    swap = True
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swap = True
        if not swap:
            break
    return L


def selectionsort(L):
    n = len(L)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if (L[j] < L[min_idx]):
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]
    return L


def insertionsort(L):
    n = len(L)
    for i in range(1, n):
        value = L[i]
        hole_idx = i
        while (hole_idx > 0 and L[hole_idx - 1] > value):
            L[hole_idx] = L[hole_idx - 1]
            hole_idx -= 1
        L[hole_idx] = value
    return L


def quicksort_inplace(L):
    quicksort_recursive(L, 0, len(L) - 1)
    return L


def quicksort_recursive(L, low, high):
    if low < high:
        par = partition(L, low, high)
        quicksort_recursive(L, low, par - 1)
        quicksort_recursive(L, par + 1, high)


def partition(L, low, high):
    pivot = L[low]
    i = high + 1
    for j in range(high, low - 1, -1):
        if L[j] > pivot:
            i -= 1
            L[i], L[j] = L[j], L[i]
    L[i - 1], L[low] = L[low], L[i - 1]
    return i - 1


def final_sort(L):
    if len(L) <= 20:
        return insertionsort(L)
    copy = final_sort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
    return L


def final_sort_copy(L):
    if len(L) <= 20:
        return insertionsort(L)
    mid = len(L)//2
    pivot = L[mid]
    L[0], L[mid] = L[mid], L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return final_sort_copy(left) + [pivot] + final_sort_copy(right)

## This algorithms performance is similar to final_sort
# def final_sort2(L):
#     copy = final_sort_copy(L)
#     for i in range(len(L)):
#         L[i] = copy[i]
#     return L
#
#
# def final_sort_copy2(L):
#     if len(L) < 2:
#         return L
#     mid = len(L)//2
#     pivot = L[mid]
#     left, right = [], []
#     for num in L[0:mid]:
#         if num < pivot:
#             left.append(num)
#         else:
#             right.append(num)
#     for num in L[(mid+1):]:
#         if num < pivot:
#             left.append(num)
#         else:
#             right.append(num)
#     return final_sort_copy2(left) + [pivot] + final_sort_copy2(right)
###########

def timetest1(runs, n, func_type):  # unsorted
    total_runtime = 0
    for _ in range(runs):
        L_unsorted = create_random_list(n)
        # L_sorted = create_near_sorted_list(n, 0.01)
        start = timeit.default_timer()
        func_type(L_unsorted)
        end = timeit.default_timer()
        total_runtime += end - start
    return total_runtime / runs


def timetest2(runs, n, func_type, factor):  # sorted
    total_runtime = 0
    for _ in range(runs):
        # L_unsorted = create_random_list(n)
        L_sorted = create_near_sorted_list(n, factor)
        start = timeit.default_timer()
        func_type(L_sorted)
        end = timeit.default_timer()
        total_runtime += end - start
    return total_runtime / runs


## Test algorithms runtime (unsorted, low range)
# for n in range(1, 21, 1):  # range(length of start_list, length of last_list, increase)
#     avg_run = 10000
#     print(n, #timetest1(avg_run, n, bubblesort_opt),
#           #timetest1(avg_run, n, selectionsort),
#           timetest1(avg_run, n, insertionsort),
#           timetest1(avg_run, n, my_quicksort),
#           timetest1(avg_run, n, final_sort))

## Test algorithms runtime (sorted)
# for n in range(1, 1000, 50): # range(length of start_list, length of last_list, increase)
#     avg_run = 50
#     factor = 0
#     print(n, timetest2(avg_run, n, bubblesort_opt, factor),
#           timetest2(avg_run, n, selectionsort, factor),
#           timetest2(avg_run, n, insertionsort, factor),
#           timetest2(avg_run, n, my_quicksort, factor))

## Test for different factors
# for i in range(1, 100, 1): # range(length of start_list, length of last_list, increase)
#     avg_run = 5000
#     factor = i * 0.005
#     n = 10
#     print(factor, timetest2(avg_run, n, bubblesort_opt, factor),
#           timetest2(avg_run, n, selectionsort, factor),
#           timetest2(avg_run, n, insertionsort, factor),
#           timetest2(avg_run, n, my_quicksort, factor))

## Test for different factors (Insertion, quicksort)
for i in range(1, 41, 1): #range(length of start_list, length of last_list, increase)
    avg_run = 1000
    factor = i * 0.005
    n = 100
    print(factor, timetest2(avg_run, n, insertionsort, factor),
          timetest2(avg_run, n, my_quicksort, factor),
          #timetest2(avg_run, n, semi_final, factor),
          timetest2(avg_run, n, final_sort, factor))

## Test bubblesort opt algorithms runtime (unsorted, sorted)
# for n in range(1, 1001, 1):  # range(length of start_list, length of last_list, increase)
#     avg_run = 5
#     factor = 0
#     print(n, timetest1(avg_run, n, my_quicksort),
#           timetest1(avg_run, n, quicksort_inplace),
#           timetest2(avg_run, n, bubblesort, factor),
#           timetest2(avg_run, n, bubblesort_opt, factor))

## Check sorting algorithms
# for _ in range(10):
#     L = create_random_list(20)
#     # print(L, bubblesort_opt(L.copy()))
#     # print(L, selectionsort(L.copy()))
#     print(L, insertionsort(L.copy()))
#     print(L, my_quicksort(L.copy()))
#     # print(L, semi_final(L.copy()))
#     print(L, final_sort(L.copy()))
