#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:24:42 2021

@author: Mingzhe Wang
"""

import statistics
import matplotlib.pyplot as plt
import timeit
from lab3 import my_quicksort
from lab3 import create_random_list
from sorts import quicksort_inplace

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
    return (total_my/runs, total_inp/runs)

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

############################# Some answers ###################################
# For "Which is better": my_quicksort is better.
# For "By how much" question: need to use fitting in excel, maybe.
# For "Which would you use in pratice": quicksort_inplace, because the space
# complexity of my_quicksort is too high. (My opinion)




    
    
    

    
    
