#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@brief: This module tests the multi-pivot functions
@author: Xing Li
"""

import matplotlib.pyplot as plt
import timeit
from lab3 import my_quicksort
from lab3 import create_random_list
from multi_pivot import dual_pivot_quicksort, tri_pivot_quicksort, quad_pivot_quicksort

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
    return (total_my/runs, total_inp/runs)

def plot(f1, f2, n_range, runs):
    t_range_my = []
    t_range_inp = []
    for n in n_range:
        t = generate(f1, f2, runs, n)
        t_range_my.append(t[0])
        t_range_inp.append(t[1])
    labels = [str(f1).split()[1], str(f2).split()[1]]
    plt.scatter(n_range, t_range_my, marker = '.', 
                label = labels[0])
    plt.scatter(n_range, t_range_inp, marker = '.', 
                label = labels[1])
    plt.xlabel("List size(n)")
    plt.ylabel("Run time(second)")
    plt.legend(loc='upper left');
    plt.savefig("Figures/multi_pivot_" + labels[0] + "_" + labels[1])
    plt.close()

n_range = [100 * _ for _ in range(100)]

plot(my_quicksort, dual_pivot_quicksort, n_range, 10)
plot(my_quicksort, tri_pivot_quicksort, n_range, 10)
plot(my_quicksort, quad_pivot_quicksort, n_range, 10)
