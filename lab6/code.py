import random
import matplotlib.pyplot as plt
import math

from rbt import *

################## PREPARE ####################

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




################# avg hiehgt of RBTs vs BSTs ############

runs = 10
rbt_height = 0
bst_height = 0
rbt_height_rng = []
bst_height_rng = []

# for _ in range(1, runs):
for run in range(runs):
     L = create_random_list(50000)
     rbtree = RBTree()
     bstree = BinarySearchTree()
     for i in L:
         rbtree.insert(i)
         bstree.insert_bst(i)
     rbt_height_rng.append(rbtree.get_height())
     bst_height_rng.append(bstree.get_height2())
     rbt_height += rbtree.get_height()
     bst_height += bstree.get_height2()
print("avg_rbt_height: ", rbt_height / runs)
print("avg_bst_height: ", bst_height / runs)

plt.scatter(list(range(runs)), rbt_height_rng, marker='.', label="RBTs")
plt.scatter(list(range(runs)), bst_height_rng, marker='.', label="BSTs")
plt.xlabel("Number of repetition(n)")
plt.ylabel("Height")
plt.legend(loc='upper left')
plt.savefig("Figures/" + "rbt_bst_avg_50000")
plt.close()



################# hiehgt of RBTs vs BSTs + sorted factor ############
rbt_height = 0
bst_height = 0
rbt_height_rng = []
bst_height_rng = []
factors = [0.02*_ for _ in range(1, 11)]
for factor in factors:    
    L = create_near_sorted_list(10000, factor)
    rbtree = RBTree()
    bstree = BinarySearchTree()
    for i in L:
        rbtree.insert(i)
        bstree.insert_bst(i)
    rbt_height_rng.append(rbtree.get_height())
    bst_height_rng.append(bstree.get_height2())
    rbt_height += rbtree.get_height()
    bst_height += bstree.get_height2()
print("avg_rbt_height: ", rbt_height / len(factors))
print("avg_bst_height: ", bst_height / len(factors))

plt.scatter(factors, rbt_height_rng, marker='.', label="RBTs")
plt.scatter(factors, bst_height_rng, marker='.', label="BSTs")
plt.xlabel("Sorted factor)")
plt.ylabel("Height")
plt.legend(loc='upper right')
plt.savefig("Figures/" + "sorted_case")
plt.close()


################ TESTING RBT ##################

# rbtree = RBTree()
# for i in range(1,10):
#     rbtree.insert(i)
#     print("Insert: ", i)
#     print(rbtree)
#     print()
# print(rbtree.get_height())

# rbtree = RBTree()
# for _ in range(1,20):
#     for i in range(1,10001,1):
#         rbtree.insert(i)    
#     print(rbtree.root)
#     print(rbtree.get_height())



##rbtree = RBTree()
##
##print("Insert 10")
##
##rbtree.insert(10)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 11")
##
##rbtree.insert(11)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 9")
##
##rbtree.insert(9)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 13")
##
##rbtree.insert(13)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 14")
##
##rbtree.insert(14)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##
##print("Insert 12")
##
##rbtree.insert(12)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##print("Insert 15")
##
##rbtree.insert(15)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 16")
##
##rbtree.insert(16)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 17")
##
##rbtree.insert(17)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##
##rbtree = RBTree()
##
##print("Insert 10")
##
##rbtree.insert(10)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 9")
##
##rbtree.insert(9)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 11")
##
##rbtree.insert(11)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 8")
##
##rbtree.insert(8)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 7")
##
##rbtree.insert(7)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##
##print("Insert 6")
##
##rbtree.insert(6)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##print("Insert 5")
##
##rbtree.insert(5)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 4")
##
##rbtree.insert(4)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##print("Insert 3")
##
##rbtree.insert(3)
##
##print(rbtree)
##
##print("root: ", rbtree.root)
##
##print("height: ",rbtree.get_height())
##
##print()
##
##
##
##
##rbtree = RBTree()
##
##for i in range(1,101,1):
##
##    rbtree.insert(i)
##
##print(rbtree.root)
##
##print(rbtree.get_height())
##
##def create_random_list(n):
##    L = []
##    for _ in range(n):
##        L.append(random.randint(1,n))
##    return L
##
### for _ in range(1, runs):
##runs = 10
##rbt_height = 0
##for run in range(runs):
##     L = create_random_list(10000)
##     rbtree = RBTree()
##     for i in L:
##         rbtree.insert(i)
##     rbt_height += rbtree.get_height()
##print("avg_rbt_height: ", rbt_height / runs)


###########################################################
