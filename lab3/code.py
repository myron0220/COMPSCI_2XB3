import statistics
import random
import math
import matplotlib.pyplot as plt
import timeit
from sorts import quicksort_inplace
from multi_pivot import dual_pivot_quicksort, tri_pivot_quicksort, quad_pivot_quicksort
from sorts import final_sort 

### Sorting algorithms ###
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


### Timing experiments 1 (quicksort_inplace)###
def test_my_quicksort_vs_quicksort_inplace(runs, n):
    total_my = 0
    total_inp = 0
    for _ in range(runs):
        ls1 = create_random_list(n)
        ls2 = ls1.copy()

        start_my = timeit.default_timer()
        my_quicksort(ls1)
        end_my = timeit.default_timer()

        start_inp = timeit.default_timer()
        quicksort_inplace(ls2)
        end_inp = timeit.default_timer()

        total_my += end_my - start_my
        total_inp += end_inp - start_inp
    return (total_my / runs, total_inp / runs)


def plot_my_quicksort_and_quicksort_inplace(n_range, runs):
    t_range_my = []
    t_range_inp = []
    for n in n_range:
        t = test_my_quicksort_vs_quicksort_inplace(runs, n)
        t_range_my.append(t[0])
        t_range_inp.append(t[1])
    # plot vs.
    plt.scatter(n_range, t_range_my, marker = '.',
                label = "my_quicksort")
    plt.scatter(n_range, t_range_inp, marker = '.',
                label = "quicksort_inplace")
    plt.legend(loc='upper left')
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.show()
    # plot how much
    by_how_much = []
    i = 0
    for n in n_range:
        ans = (t_range_inp[i] - t_range_my[i]) / t_range_inp[i] * 100
        by_how_much.append(ans)
        i += 1
    plt.scatter(n_range, by_how_much, marker = '.',
                label = "median: " + str(statistics.median(by_how_much)))
    plt.legend(loc='lower right')
    plt.xlabel("List size(n)")
    plt.ylabel("Faster by percentage(%)")
    plt.show()

n_range = [100 * _ for _ in range(100)]
plot_my_quicksort_and_quicksort_inplace(n_range, 10)


### Timing experiments 2 (Multi pivots) ###
def generate(f1, f2, runs, n):
    total_my = 0
    total_inp = 0
    for _ in range(runs):
        ls1 = create_random_list(n)
        ls2 = ls1.copy()

        start_my = timeit.default_timer()
        f1(ls1)
        end_my = timeit.default_timer()

        start_inp = timeit.default_timer()
        f2(ls2)
        end_inp = timeit.default_timer()

        total_my += end_my - start_my
        total_inp += end_inp - start_inp
    return (total_my / runs, total_inp / runs)


def plot(f1, f2, n_range, runs):
    t_range_my = []
    t_range_inp = []
    for n in n_range:
        t = generate(f1, f2, runs, n)
        t_range_my.append(t[0])
        t_range_inp.append(t[1])
    labels = [str(f1).split()[1], str(f2).split()[1]]
    plt.scatter(n_range, t_range_my, marker='.',
                label=labels[0])
    plt.scatter(n_range, t_range_inp, marker='.',
                label=labels[1])
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left');
    plt.savefig("Figures/multi_pivot_" + labels[0] + "_" + labels[1])
    plt.close()

# n_range = [100 * _ for _ in range(100)]
# plot(my_quicksort, dual_pivot_quicksort, n_range, 10)
# plot(my_quicksort, tri_pivot_quicksort, n_range, 10)
# plot(my_quicksort, quad_pivot_quicksort, n_range, 10)


### Timing experiments 3 (my_quicksort) ###
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
for n in range(1, 21, 1):  # range(length of start_list, length of last_list, increase)
    avg_run = 10000
    print(n, #timetest1(avg_run, n, bubblesort_opt),
          #timetest1(avg_run, n, selectionsort),
          timetest1(avg_run, n, insertionsort),
          timetest1(avg_run, n, my_quicksort),
          timetest1(avg_run, n, final_sort))

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
# for i in range(1, 41, 1): #range(length of start_list, length of last_list, increase)
#     avg_run = 1000
#     factor = i * 0.005
#     n = 100
#     print(factor, timetest2(avg_run, n, insertionsort, factor),
#           timetest2(avg_run, n, my_quicksort, factor),
#           #timetest2(avg_run, n, semi_final, factor),
#           timetest2(avg_run, n, final_sort, factor))

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
