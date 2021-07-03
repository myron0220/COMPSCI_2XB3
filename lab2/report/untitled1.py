#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:43:41 2021

@author: kidsama
"""

import time
def list_by_append(n):
    '''Creates a list & appends n elements'''
    lst = []
    for i in range(n):
        lst.append(n)
    return lst
def list_by_extend(n):
    '''Creates a list & extends it with n elements'''
    lst = []
    lst.extend(range(n))
    return lst
# Compare runtime of both methods
list_sizes = [i * 10000 for i in range(100)]
append_runtimes = []
extend_runtimes = []
for size in list_sizes:
    # Get time stamps
    time_0 = time.time()
    list_by_append(size)
    time_1 = time.time()
    list_by_extend(size)
    time_2 = time.time()
    # Calculate runtimes
    append_runtimes.append((size, time_1 - time_0))
    extend_runtimes.append((size, time_2 - time_1))
# Plot everything
import matplotlib.pyplot as plt
import numpy as np
append_runtimes = np.array(append_runtimes)
extend_runtimes = np.array(extend_runtimes)
print(append_runtimes)
print(extend_runtimes)
plt.plot(append_runtimes[:,0], append_runtimes[:,1], label='append()')
plt.plot(extend_runtimes[:,0], extend_runtimes[:,1], label='extend()')
plt.xlabel('list size')
plt.ylabel('runtime (seconds)')
plt.legend()
plt.savefig('append_vs_extend.jpg')
plt.show()