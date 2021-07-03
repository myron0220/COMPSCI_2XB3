# @@file sorts.py
# @brief All sort methods used in this lab are here except for lab4.py
#        original ones.
# @author Hyosik Moon, Mengzhe Wang, Xing Li
# @date Feb. 17, 2021

import random
from lab4 import *
#from code import *
    

############################## mergesort_bottom_up ##############################
def merge_bottom(L, start, mid, end):
    i = start
    j = mid
    tl = []
    while i < mid or j < end:
        if i >= mid:
            tl.append(L[j])
            j += 1
        elif j >= end:
            tl.append(L[i])
            i += 1
        else:
            if L[i] <= L[j]:
                tl.append(L[i])
                i += 1
            else:
                tl.append(L[j])
                j += 1
    for i in range(end - start):
        L[start + i] = tl[i]
        
def mergesort_bottom_up(L):
    N = len(L)
    r = 1
    while r < N:
        for i in range(N //(2 * r) + 1):
            end = min((i + 1) * 2 * r, N)
            start = i * 2 * r
            mid = start + r
            if mid < end:
                merge_bottom(L, start, mid, end)
        r *= 2

############################## mergesort_threeway ###############################
def merge_three(left, mid, right):
    L = []
    i = j = k = 0

    while i < len(left) or j < len(mid) or k < len(right):
        if i >= len(left):
            if j >= len(mid):
                L.append(right[k])
                k += 1
            else:
                if k >= len(right):
                    L.append(mid[j])
                    j += 1
                else:
                    if mid[j] <= right[k]:
                        L.append(mid[j])
                        j += 1
                    else:
                        L.append(right[k])
                        k += 1
        else:
            if j >= len(mid):
                if k >= len(right):
                    L.append(left[i])
                    i += 1
                else:
                    if left[i] <= right[k]:
                        L.append(left[i])
                        i += 1
                    else:
                        L.append(right[k])
                        k += 1
            else:
                if k >= len(right):
                    if left[i] <= mid[j]:
                        L.append(left[i])
                        i += 1
                    else:
                        L.append(mid[j])
                        j += 1
                else:
                    if left[i] <= mid[j]:
                        if right[k] <= left[i]:
                            L.append(right[k])
                            k += 1
                        else:
                            L.append(left[i])
                            i += 1
                    else:
                        if right[k] <= mid[j]:
                            L.append(right[k])
                            k += 1
                        else:
                            L.append(mid[j])
                            j += 1
    return L

def mergesort_three(L):
    
    if len(L) <= 1:
        return
    l = len(L) // 3
    r = 2 * l + (len(L) % 3) // 2
    left, mid, right = L[:l], L[l:r], L[r:]
    
    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)
    
    temp = merge_three(left, mid, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


############################## mergesort_opt ###############################

# 1. mergesort vs mergesort_three (m < m_t) 
# 2. mergersort_three vs mergesort_bottom_up (m_t < m_b)
# 3. mergesort_bottom_up vs mergesort_three_bottom_up (m_b < m_t_b)

def merge_three_bottom_up(L, start, mid1, mid2, end):
    i = start
    j = mid1
    k = mid2
    temp = []
    while i < mid1 or j < mid2 or k < end:
        if i >= mid1:
            if j >= mid2:
                temp.append(L[k])
                k += 1
            elif k >= end:
                temp.append(L[j])
                j += 1
            else:
                if L[j] <= L[k]:
                    temp.append(L[j])
                    j += 1 
                else:
                    temp.append(L[k])
                    k += 1    
        elif j >= mid2:
            if k >= end:
                temp.append(L[i])
                i += 1
            else:
                if L[i] <= L[k]:
                    temp.append(L[i])
                    i += 1
                else:
                    temp.append(L[k])
                    k += 1
        else:
            if k >= end:
                if L[i] <= L[j]:
                    temp.append(L[i])
                    i += 1
                else:
                    temp.append(L[j])
                    j += 1
            else:
                if L[i] <= L[j]:
                    if L[k] <= L[i]:
                        temp.append(L[k])
                        k += 1
                    else:
                        temp.append(L[i])
                        i += 1
                else:
                    if L[k] <= L[j]:
                        temp.append(L[k])
                        k += 1
                    else:
                        temp.append(L[j])
                        j += 1
    for i in range(end - start):
        L[start + i] = temp[i]
        
def mergesort_three_bottom_up(L):
    N = len(L)
    r = 1
    while r < N:
        for i in range(N //(3 * r) + 1):
            start = i * r * 3
            mid1 = start + r
            mid2 = min(start + 2*r, N)
            end = min(start + 3*r, N)
            if mid1 < mid2:
                merge_three_bottom_up(L, start, mid1, mid2, end)
        r *= 3

# ####################### test mergesort_three_bottom_up mannually #######################
# L = create_random_list(20)
# print("Original list: ")
# print(L)
# print()
# mergesort_three_bottom_up(L)
# print("After mergesort_three: ")
# print(L)
# print()

####################### test mergesort_three mannually #######################
# L = create_random_list(3)
# print("Original list: ")
# print(L)
# print()
# mergesort_three(L)
# print("After mergesort_three: ")
# print(L)
# print()

##################### test mergesort_three vs mergesort ######################
# L_a = create_random_list(20)
# print("Original L_a: ")
# print(L_a)
# L_b = L_a[:]
# print("Original L_b: ")
# print(L_b)
# mergesort(L_a)
# print("mergesort L_a: ")
# print(L_a)
# mergesort_three(L_b)
# print("mergesort_three L_b: ")
# print(L_b)
# for i in range(len(L_a)):
#     if (L_a[i] != L_b[i]):
#         print("Fail")
# print("Pass")

###################### test for validity of mergesort_three ###################
# for _ in range(10000):
#     n = random.randint(0, 1000)
#     L_a = create_random_list(n)
#     L_b = L_a.copy()
#     L_a.sort()
#     mergesort_three(L_b)
#     for i in range(n):
#         assert L_a[i] == L_b[i]
# print("PASS")

############################# test mergesort_bottom_up #########################
# def test_mergesort_bottom_up():
#     test_list = [9, 1, 5, 2, 11, 18, 7, 23, 13, 0, 4]
#     print(test_list)
#     mergesort(test_list)
#     print(test_list)
#     test_list = [9, 1, 5, 2, 11, 18, 7, 23, 13, 0, 4]
#     mergesort_bottom_up(test_list)
#     print(test_list)


