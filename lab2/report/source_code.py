#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:52:22 2021

@author: kidsama
"""
import matplotlib.pyplot as plt
import random
import timeit
import xlsxwriter

data_path = r'/Users/kidsama/Documents/COMPSCI 2XB3/2xb3_lab2/list_data.xlsx'
workbook = xlsxwriter.Workbook(data_path)

def create_random_list(n, upper):
    return [random.randint(0, upper) for _ in range(n)]

# def copy test
def copy_test(runs, n, upper):
    total = 0
    for _ in range(runs):
        ls = create_random_list(n, upper)
        start = timeit.default_timer()
        ls.copy()
        end = timeit.default_timer()
        total += end - start
    return total/runs

# plot copy test
def plot_copy_test():
    x = [_ * 100 for _ in range(100)]
    y = []
    for _ in x:
        y.append(copy_test(100, _, 500))
    plt.scatter(x, y, marker='.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of copy())')
    copy_test_data = workbook.add_worksheet("copy_test_data")
    copy_test_data.write(0, 0, "N")
    copy_test_data.write_column(1, 0, x)
    copy_test_data.write(0, 1, "T")
    copy_test_data.write_column(1, 1, y)
        
# lookups test
def plot_lookups_test():
    ls = create_random_list(1000000, 1000000)
    x = range(1000000)
    y = []
    for i in x:
        start = timeit.default_timer()
        ls[i]
        end = timeit.default_timer()
        y.append(end - start)
    plt.scatter(x, y, marker='.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of lookups')

def plot_lookups_test_fixed(runs):
    ls = create_random_list(1000000, 1000000)
    x = range(1000000)
    y = []
    for i in x:
        for _ in range(runs):
            total = 0
            start = timeit.default_timer()
            ls[i]
            end = timeit.default_timer()
            total += end - start
        y.append(total/runs)
    plt.scatter(x, y, marker='.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of lookups')
    copy_test_data = workbook.add_worksheet("lookups_test_data")
    copy_test_data.write(0, 0, "N")
    copy_test_data.write_column(1, 0, x)
    copy_test_data.write(0, 1, "T")
    copy_test_data.write_column(1, 1, y)

def plot_append_test_fixed(runs):
    x = range(1000000)
    y = []
    ls = []
    for i in x:
        for _ in range(runs):
            total = 0
            value = random.randint(0, 1000000)
            start = timeit.default_timer()
            ls.append(value)
            end = timeit.default_timer()
            total += end - start
        y.append(total/runs)
    plt.scatter(x, y, marker='.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of append()')
    copy_test_data = workbook.add_worksheet("append_test_data1")
    copy_test_data.write(0, 0, "N")
    copy_test_data.write_column(1, 0, x)
    copy_test_data.write(0, 1, "T")
    copy_test_data.write_column(1, 1, y)
        
def plot_append_ls2_test(runs):
    x = [_ * 1000 for _ in range(100)]
    y = []
    for n in x:
        for i in range(runs):
            total = 0
            ls = []
            ls2 = create_random_list(n, n)
            start = timeit.default_timer()
            ls.append(ls2)
            end = timeit.default_timer()
            total += end - start
        y.append(total/runs)
    plt.scatter(x, y, marker = '.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of append()')
    copy_test_data = workbook.add_worksheet("append_test_data2")
    copy_test_data.write(0, 0, "N")
    copy_test_data.write_column(1, 0, x)
    copy_test_data.write(0, 1, "T")
    copy_test_data.write_column(1, 1, y)

def plot_append_ls3_test(runs):
    x = [_ * 1000 for _ in range(100)]
    y = []
    for n in x:
        for i in range(runs):
            total = 0
            ls = create_random_list(2000, 2000)
            ls2 = create_random_list(n, n)
            start = timeit.default_timer()
            ls.append(ls2)
            end = timeit.default_timer()
            total += end - start
        y.append(total/runs)
    plt.scatter(x, y, marker = '.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of append()')
    copy_test_data = workbook.add_worksheet("append_test_data3")
    copy_test_data.write(0, 0, "N")
    copy_test_data.write_column(1, 0, x)
    copy_test_data.write(0, 1, "T")
    copy_test_data.write_column(1, 1, y)

    
def plot_append_ls4_test(runs):
    x = [_ * 1000 for _ in range(100)]
    y = []
    for n in x:
        for i in range(runs):
            total = 0
            ls = create_random_list(n, n)
            ls2 = create_random_list(n, n)
            start = timeit.default_timer()
            ls.append(ls2)
            end = timeit.default_timer()
            total += end - start
        y.append(total/runs)
    plt.scatter(x, y, marker = '.')
    plt.xlabel('N ')
    plt.ylabel('T (s)')
    plt.title('Time complexity of append()')
    copy_test_data = workbook.add_worksheet("append_test_data4")
    copy_test_data.write(0, 0, "N")
    copy_test_data.write_column(1, 0, x)
    copy_test_data.write(0, 1, "T")
    copy_test_data.write_column(1, 1, y)

# test
# plot_copy_test()
# plot_lookups_test()
# plot_lookups_test_fixed(500)
# plot_append_test_fixed(1)
# plot_append_test_fixed(100)
# plot_append_ls2_test(1)
# plot_append_ls3_test(1)
# plot_append_ls4_test(1)

workbook.close()




