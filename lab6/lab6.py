import random
import matplotlib.pyplot as plt
import math


class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    # def rotate_right(self):
    #     y = self.left
    #     self.left = y.right
    #     if y.right.value != None:
    #         y.right.parent = self
    #     y.parent = self.parent
    #     if self.parent == None: #//self is root
    #         y.parent = None
    #     elif self.is_left_child():
    #         self.parent.left = y
    #     else: #// self is right child
    #         self.parent.right = y
    #     y.right = self
    #     self.parent = y

    # def rotate_left(self):
    #     y = self.right
    #     self.right = y.left
    #     if y.left.value != None:
    #         y.left.parent = self
    #     y.parent = self.parent
    #     if self.parent == None: #//self is root
    #         y.parent = None
    #     elif self.is_left_child():
    #         self.parent.left = y
    #     else: #// self is right child
    #         self.parent.right = y
    #     y.left = self
    #     self.parent = y


class RBTree:

    def __init__(self):
        nil_node = RBNode(None)
        nil_node.colour = "B"
        self.NIL = nil_node
        self.root = self.NIL

    def is_empty(self):
        return self.root == self.NIL 

    def get_root(self):
        return self.root    

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root) - 1

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert_rbt(self, value):
        in_node = RBNode(value)  
        in_node.left = self.NIL
        in_node.right = self.NIL  
        in_node.parent = self.NIL 
        if self.is_empty():
            # print("is_empty sequence")
            self.root = in_node
            self.root.right = self.NIL
            self.root.left = self.NIL
            self.root.parent = self.NIL 
            self.root.make_black()
        else:
            self.__insert(self.root, in_node)

    def __insert(self, node, in_node):
        # print(node, "root")
        if in_node.value < node.value:
            if node.left == self.NIL:
                node.left = in_node
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, in_node)
        else:
            if node.right == self.NIL:
                node.right = in_node
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, in_node)

    def fix(self, in_node):
        #You may alter code in this method if you wish, it's merely a guide.
        if in_node.parent == self.NIL:
            in_node.make_black()
        while in_node != self.NIL and in_node.parent != self.root and in_node.parent.is_red():
            if in_node.parent == in_node.parent.parent.left:   #in_node.parent is left child
                y = in_node.parent.parent.right    #uncle of node
                if y.is_red():      #case1: uncle is red
                    in_node.parent.colour = "B"
                    y.colour = "B"
                    in_node.parent.parent.colour = "R"
                    in_node = in_node.parent.parent
                else:       #case2 or case3
                    if in_node == in_node.parent.right:   #case2
                        in_node = in_node.parent
                        self.rotate_left(in_node)
                    # case3
                    in_node.parent.colour = "B"
                    in_node.parent.parent.colour = "R"
                    self.rotate_right(in_node.parent.parent)
            else: #in_node.parent is the right child    
                y = in_node.parent.parent.left     #uncle of node
                if y.colour == "R":
                    in_node.parent.colour = "B"
                    y.colour = "B"
                    in_node.parent.parent.colour = "R"
                    in_node = in_node.parent.parent
                else:
                    if in_node == in_node.parent.left:
                        in_node = in_node.parent
                        self.rotate_right(in_node)  
                    in_node.parent.colour = "B"
                    in_node.parent.parent.colour = "R"
                    self.rotate_left(in_node.parent.parent)
        self.root.make_black()
        # print("self.root", self.root)

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL: #//self is root
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else: #// self is right child
            x.parent.left = y
        y.right = x
        x.parent = y

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL: #//self is root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: #// self is right child
            x.parent.right = y
        y.left = x
        x.parent = y

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


# ##############
# rbtree = RBTree()
# print("Insert 10")
# rbtree.insert(10)
# print(rbtree)
# print("root: ", rbtree.get_root())
# print("height: ",rbtree.get_height())
# print()

# print("Insert 11")
# rbtree.insert(11)
# print(rbtree)
# print("root: ", rbtree.get_root())
# print("height: ",rbtree.get_height())
# print()

# print("Insert 12")
# rbtree.insert(12)
# print(rbtree)
# print("root: ", rbtree.get_root())
# print("height: ",rbtree.get_height())
# print()

# print("Insert 13")
# rbtree.insert(13)
# print(rbtree)
# print("root: ", rbtree.get_root())
# print("height: ",rbtree.get_height())
# print()

# print("Insert 14")
# rbtree.insert(14)
# print(rbtree)
# print("root: ", rbtree.get_root())
# print("height: ",rbtree.get_height())
# print()

# for i in range(1,10001,1):
#     rbtree.insert(i)
# # print(rbtree)
# # print("root: ", rbtree.get_root())
# # print("height: ",rbtree.get_height())
# print(rbtree.get_root())

# rbtree = RBTree()
# # for _ in range(1,11):
# for i in range(1,10001,1):
#     rbtree.insert(i)
# print(rbtree.get_root())
# print(rbtree.get_height())


###########################################################


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None    

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def insert_bst(self, n):
        n = Node(n)
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left    
            else:
                temp = temp.right

        n.parent = y

        if y == None: #newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent

    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)

        elif z.right == None:
            self.transplant(z, z.left)

        else:
            y = self.minimum(z.right) #minimum element in right subtree
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)

    def get_height2(self):
        if self.root == None:
            return 0
        return self.__get_height2(self.root)

    def __get_height2(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height2(node.left), self.__get_height2(node.right))

################## TEST ####################

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


# bstree = BinarySearchTree()
# for i in create_random_list(5):
#     bstree.insert(i)    
# print(bstree.inorder(bstree.root))
# print(bstree.get_height2())

################# avg hiehgt of RBTs vs BSTs ############

# runs = 10
# rbt_height = 0
# bst_height = 0
# rbt_height_rng = []
# bst_height_rng = []

# # for _ in range(1, runs):
# for run in range(runs):
#     L = create_random_list(50000)
#     rbtree = RBTree()
#     bstree = BinarySearchTree()
#     for i in L:
#         rbtree.insert_rbt(i)
#         bstree.insert_bst(i)
#     rbt_height_rng.append(rbtree.get_height())
#     bst_height_rng.append(bstree.get_height2())
#     rbt_height += rbtree.get_height()
#     bst_height += bstree.get_height2()
# print("avg_rbt_height: ", rbt_height / runs)
# print("avg_bst_height: ", bst_height / runs)

# plt.scatter(list(range(runs)), rbt_height_rng, marker='.', label="RBTs")
# plt.scatter(list(range(runs)), bst_height_rng, marker='.', label="BSTs")
# plt.xlabel("Number of repetition(n)")
# plt.ylabel("Hieght")
# plt.legend(loc='upper left')
# plt.savefig("Figures/" + "RBTs_vs_BSTs_2")
# plt.close()



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
        rbtree.insert_rbt(i)
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
plt.savefig("Figures/" + "RBTs_vs_BSTs_sorted3")
plt.close()