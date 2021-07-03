# @@file code.py
# @brief code for experiments, testing and time complexity analysis
# @author Hyosik Moon, Mingzhe Wang, Xing Li
# @date Feb. 21, 2021

import math
import random
import timeit

import matplotlib.pyplot as plt

from heap import *

###################### general function for test and plot ######################
   
def compare_heap3(n, runs):
    total_f1 = 0
    for _ in range(runs):
        L = create_random_list(n)
        L = sorted(L)
        heap = Heap(L)

        start_f1 = timeit.default_timer()
        heap.build_heap3()
        end_f1 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
    return total_f1 / runs
    
def plot_heap3(n_range, runs):
    t_range_f1 = []
    for n in n_range:
        t = compare_heap3(n, runs)
        t_range_f1.append(t)
        print(n, t)
    labels = "Sink_top_down_sorted"
    plt.scatter(n_range, t_range_f1, marker='.',
                label=labels)
    plt.xlabel("Number of elements(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/" + labels)
    plt.close()
    
def compare_heap2(n, runs):
    total_f1 = 0
    for _ in range(runs):
        L = create_random_list(n)
        heap = Heap(L)

        start_f1 = timeit.default_timer()
        heap.build_heap2()
        end_f1 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
    return total_f1 / runs
    
def plot_heap2(n_range, runs):
    t_range_f1 = []
    for n in n_range:
        t = compare_heap2(n, runs)
        t_range_f1.append(t)
        print(n, t)
    labels = "Brick_by_brick"
    plt.scatter(n_range, t_range_f1, marker='.',
                label=labels)
    plt.xlabel("Number of elements(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/" + labels)
    plt.close()
    
def compare_heap1(n, runs):
    total_f1 = 0
    for _ in range(runs):
        L = create_random_list(n)
        heap = Heap(L)

        start_f1 = timeit.default_timer()
        heap.build_heap1()
        end_f1 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
    return total_f1 / runs
    
def plot_heap1(n_range, runs):
    t_range_f1 = []
    for n in n_range:
        t = compare_heap1(n, runs)
        t_range_f1.append(t)
        print(n, t)
    labels = "Bottom_up"
    plt.scatter(n_range, t_range_f1, marker='.',
                label=labels)
    plt.xlabel("Number of elements(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/" + labels)
    plt.close()

def compare(f1, f2, runs, n):
    total_f1 = 0
    total_f2 = 0
    for _ in range(runs):
        ls1 = create_random_list(n)
        ls2 = ls1.copy()

        start_f1 = timeit.default_timer()
        f1(ls1)
        end_f1 = timeit.default_timer()

        start_f2 = timeit.default_timer()
        f2(ls2)
        end_f2 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
        total_f2 += end_f2 - start_f2
    return (total_f1 / runs, total_f2 / runs)
    
def plot(f1, f2, n_range, runs):
    t_range_f1 = []
    t_range_f2 = []
    t_range_comp = []
    for n in n_range:
        t = compare(f1, f2, runs, n)
        t_range_f1.append(t[0])
        t_range_f2.append(t[1])
        t_range_comp.append((t[0]-t[1])/t[1])
    labels = [str(f1).split()[1], str(f2).split()[1]]
    plt.scatter(n_range, t_range_f1, marker='.',
                label=labels[0])
    plt.scatter(n_range, t_range_f2, marker='.',
                label=labels[1])
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/" + labels[0] + "_vs_" + labels[1])
    plt.close()
    comp_result = sum(t_range_comp)/len(t_range_comp) * 100
    print(labels[1] + " is " + str(comp_result) + "% faster than " + labels[0])

def compare3(f1, f2, f3, runs, n):
    total_f1 = 0
    total_f2 = 0
    total_f3 = 0 #
    for _ in range(runs):
        ls1 = create_random_list(n)
        ls2 = ls1.copy()
        ls3 = ls1.copy() #

        start_f1 = timeit.default_timer()
        f1(ls1)
        end_f1 = timeit.default_timer()

        start_f2 = timeit.default_timer()
        f2(ls2)
        end_f2 = timeit.default_timer()

        start_f3 = timeit.default_timer() #
        f3(ls3)
        end_f3 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
        total_f2 += end_f2 - start_f2
        total_f3 += end_f3 - start_f3 #
    return (total_f1 / runs, total_f2 / runs, total_f3 / runs) #
    
def plot3(f1, f2, f3, n_range, runs):
    t_range_f1 = []
    t_range_f2 = []
    t_range_f3 = [] #
    t_range_comp = []
    for n in n_range:
        t = compare3(f1, f2, f3, runs, n)
        t_range_f1.append(t[0])
        t_range_f2.append(t[1])
        t_range_f3.append(t[2]) #
        t_range_comp.append((t[0]-t[2])/t[0])
        print(n, t[0], t[1], t[2]) #
    labels = [str(f1).split()[1], str(f2).split()[1], str(f3).split()[1]]
    plt.scatter(n_range, t_range_f1, marker='.',
                label=labels[0])
    plt.scatter(n_range, t_range_f2, marker='.',
                label=labels[1])
    plt.scatter(n_range, t_range_f3, marker='.',
                label=labels[2])    
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/Test/" + labels[0] + "_vs_" + labels[1] + "_vs_" + labels[2] + "_2")
    plt.close()
    comp_result = sum(t_range_comp)/len(t_range_comp) * 100
    print(labels[2] + " is " + str(comp_result) + "% faster than " + labels[0])

def compare1(f1, runs, size, factor):
    total_f1 = 0
    for _ in range(runs):
        ls1 = create_near_sorted_list(size, factor)

        start_f1 = timeit.default_timer()
        f1(ls1)
        end_f1 = timeit.default_timer()

        total_f1 += end_f1 - start_f1
    return total_f1 / runs 
    
def plot1(f1, f_range, size, runs):
    f_range_f1 = []
    for factor in f_range:
        t = compare1(f1, runs, size, factor)
        f_range_f1.append(t)
        print(factor, t) 
    labels = [str(f1).split()[1]]
    
    plt.scatter(f_range, f_range_f1, marker='.',
                label=labels[0])
    plt.xlabel("Factor")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/Test/" + labels[0] + "Factor")
    plt.close()

def plot2(f1, f_range, size, runs):
    f_range_f1 = []
    for factor in f_range:
        t = compare1(f1, runs, size, factor)
        f_range_f1.append(t)
        print(factor, t) 
    labels = [str(f1).split()[1]]
    
    plt.scatter(f_range, f_range_f1, marker='.',
                label=labels[0])
    plt.xlabel("Factor")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left')
    plt.savefig("Figures/Test/" + labels[0] + "_factor1")
    plt.close()

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

######### plot experiment result of build_heap1 ############
# n_range = [100 * _ for _ in range(200)]
# plot_heap1(n_range, 5)

######### plot experiment result of build_heap2 ############
# n_range = [100 * _ for _ in range(200)]
# plot_heap2(n_range, 5)

######### plot experiment result of build_heap3 ############
n_range = [100 * _ for _ in range(200)]
plot_heap3(n_range, 5)

# L = [12, 13, 7, 14, 9, 5, 2, 15, 11, 10, 8, 6, 4, 3, 1, 16]
# heap = Heap(L)
# print(heap)
# heap.build_heap3()
# print(heap)

################# plot experiment result of mergesort_bottom_up() ############
# n_range = [100 * _ for _ in range(200)]
# plot(mergesort, mergesort_bottom_up, n_range, 5)

########## plot experiment result of mergesort vs mergesort_three ############
#n_range = [100 * _ for _ in range(200)]
#plot(mergesort, mergesort_three, n_range, 5)ß

# ################# plot experiment result of  ################
# n_range = [100 * _ for _ in range(200)]
# plot3(mergesort_bottom_up, mergesort_three, mergesort_three_bottom_up, n_range, 5)

# ######### plot experiment result of  ################
# f_range = [0.02 * i for i in range(1, 26)]
# plot2(mergesort_three_bottom_up, f_range, 20000, 30)
