<<<<<<< HEAD
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

    def rotate_right(self):
        y = self.left
        self.left = y.right
        if y.right != None:
            y.right.parent = self
        y.parent = self.parent
        if self.parent == None: #self is root
            y.parent = None
        elif self.is_left_child():
            self.parent.left = y
        else: # self is right child
            self.parent.right = y
        y.right = self
        self.parent = y


    def rotate_left(self):
        y = self.right
        self.right = y.left
        if y.left != None:
            y.left.parent = self
        y.parent = self.parent
        if self.parent == None: #self is root
            y.parent = None
        elif self.is_left_child():
            self.parent.left = y
        else: # self is right child
            self.parent.right = y
        y.left = self
        self.parent = y


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            if node.parent == node.parent.parent.left:   #node.parent is left child
                y = node.parent.parent.right    #uncle of node
                if y != None and y.is_red():      #case1: uncle is red
                    node.parent.colour = "B"
                    y.colour = "B"
                    node.parent.parent.colour = "R"
                    node = node.parent.parent
                else:       #case2 or case3
                    if node == node.parent.right:   #case2
                        node = node.parent
                        node.rotate_left()
                    # case3
                    node.parent.colour = "B"
                    node.parent.parent.colour = "R"
                    node.parent.parent.rotate_right()
            else: #node.parent is the right child
                y = node.parent.parent.left     #uncle of node
                if y != None and y.is_red():
                    node.parent.colour = "B"
                    y.colour = "B"
                    node.parent.parent.colour = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        node.rotate_right()
                    node.parent.colour = "B"
                    node.parent.parent.colour = "R"
                    node.parent.parent.rotate_left()
        if node.parent != None and node.parent.parent == None:
            self.root = node.parent 
        self.root.make_black()
                    
        
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


 ##############

rbtree = RBTree()

print("Insert 10")

rbtree.insert(10)

print(rbtree)

print("root: ", rbtree.root)

print("height: ",rbtree.get_height())

print()



# print("Insert 11")

# rbtree.insert(11)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()



# print("Insert 9")

# rbtree.insert(9)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()



# print("Insert 13")

# rbtree.insert(13)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()



# print("Insert 14")

# rbtree.insert(14)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()




# print("Insert 12")

# rbtree.insert(12)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()


# print("Insert 15")

# rbtree.insert(15)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()



# print("Insert 16")

# rbtree.insert(16)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()



# print("Insert 17")

# rbtree.insert(17)

# print(rbtree)

# print("root: ", rbtree.root)

# print("height: ",rbtree.get_height())

# print()

## for i in range(1,10001,1):

##     rbtree.insert(i)

## # print(rbtree)

## # print("root: ", rbtree.get_root())

## # print("height: ",rbtree.get_height())

## print(rbtree.get_root())

##

rbtree = RBTree()

# for _ in range(1,11):

for i in range(1,10001,1):

    rbtree.insert(i)

# print(rbtree.get_root())

print(rbtree.get_height())
=======
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

    def rotate_right(self):
        y = self.left
        self.left = y.right
        if y.right != None:
            y.right.parent = self
        y.parent = self.parent
        if self.parent == None: #self is root
            y.parent = None
        elif self.is_left_child():
            self.parent.left = y
        else: # self is right child
            self.parent.right = y
        y.right = self
        self.parent = y


    def rotate_left(self):
        y = self.right
        self.right = y.left
        if y.left != None:
            y.left.parent = self
        y.parent = self.parent
        if self.parent == None: #self is root
            y.parent = None
        elif self.is_left_child():
            self.parent.left = y
        else: # self is right child
            self.parent.right = y
        y.left = self
        self.parent = y


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            self.root = node
        while node != None and node.parent != None and node.parent.is_red():            
            if node.parent.is_left_child():   
                y = node.get_uncle()    
                if y != None and y.is_red():      #case1: uncle is red
                    node.parent.colour = "B"
                    y.colour = "B"
                    node.parent.parent.colour = "R"
                    node = node.parent.parent
                else:       #case2 or case3: uncle is black or None
                    if node.is_right_child():   #case2
                        node = node.parent
                        node.rotate_left()
                    # case3
                    node.parent.colour = "B"
                    node.parent.parent.colour = "R"
                    node.parent.parent.rotate_right()
            else: # node.parent is right child. Symmetric to the code above
                y = node.get_uncle()    
                if y != None and y.is_red():
                    node.parent.colour = "B"
                    y.colour = "B"
                    node.parent.parent.colour = "R"
                    node = node.parent.parent
                else:
                    if node.is_left_child():
                        node = node.parent
                        node.rotate_right()
                    node.parent.colour = "B"
                    node.parent.parent.colour = "R"
                    node.parent.parent.rotate_left()
        if node.parent != None and node.parent.parent == None:
            self.root = node.parent 
        self.root.make_black()
                    
        
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


 ##############
rbtree = RBTree()
print("Insert 10")
rbtree.insert(10)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 11")
rbtree.insert(11)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 9")
rbtree.insert(9)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 13")
rbtree.insert(13)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 14")
rbtree.insert(14)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


print("Insert 12")
rbtree.insert(12)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 15")
rbtree.insert(15)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


print("Insert 16")
rbtree.insert(16)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


print("Insert 17")
rbtree.insert(17)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()



rbtree = RBTree()
print("Insert 10")
rbtree.insert(10)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 9")
rbtree.insert(9)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 11")
rbtree.insert(11)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 8")
rbtree.insert(8)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 7")
rbtree.insert(7)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


print("Insert 6")
rbtree.insert(6)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()

print("Insert 5")
rbtree.insert(5)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


print("Insert 4")
rbtree.insert(4)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


print("Insert 3")
rbtree.insert(3)
print(rbtree)
print("root: ", rbtree.root)
print("height: ",rbtree.get_height())
print()


rbtree = RBTree()
for i in range(1,101,1):
    rbtree.insert(i)
print(rbtree.root)
print(rbtree.get_height())

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

# for _ in range(1, runs):
runs = 10
rbt_height = 0
for run in range(runs):
     L = create_random_list(10000)
     rbtree = RBTree()
     for i in L:
         rbtree.insert(i)
     rbt_height += rbtree.get_height()
print("avg_rbt_height: ", rbt_height / runs)

>>>>>>> 149dc3acda9ae9f86e10762b25b6863744a0fd68
