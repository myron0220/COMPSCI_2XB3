#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:47:40 2021
@author: Mingzhe Wang, Hyosik Moon, Xing Li
"""

#@@ brief This function inplace quicksort
#@  param L The list to be sorted
#@  param low First index of a list
#@  param high Last index of a list
#@  return partition index
# note: Always pick first element as pivot. (We want to control vairables in 
#       our experiment, so it it better to keep consistent with my_quicksort).
def quicksort_inplace(L):
    quicksort_recursive(L, 0, len(L) - 1)
    
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
            L[i], L[j] = L[j], L[i] #swap
    L[i - 1], L[low] = L[low], L[i - 1] #swap
    return i - 1


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


def tri_pivot_quicksort(L):
    copy = quicksort_copy(L, 3)
    for i in range(len(L)):
        L[i] = copy[i]


def quad_pivot_quicksort(L):
    copy = quicksort_copy(L, 4)
    for i in range(len(L)):
        L[i] = copy[i]

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

#@@ brief This function is the optimized quicksort
#@  param L The list to be sorted
#@  return sorted list
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