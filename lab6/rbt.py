# @@file rbt.py
# @author Hyosik Moon, Mingzhe Wang, Xing Li
# @date Mar. 5, 2021


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
        # The root may change only when node.parent.parent is rotating, after that rotation, node.parent may become root and the loop ends. Therefore we only need to use the condition below to check and change root accordingly.
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
      
        # Create an empty queue for level order traversal 
        q = []
          
        # Enqueue Root and Initialize Height  
        q.append(self.root) 
        height = 0 
      
        while(True): 
              
            # nodeCount(queue size) indicates number of nodes 
            # at current level 
            nodeCount = len(q) 
            if nodeCount == 0 : 
                return height  
          
            height += 1 
      
            # Dequeue all nodes of current level and Enqueue 
            # all nodes of next level 
            while(nodeCount > 0): 
                node = q[0] 
                q.pop(0) 
                if node.left is not None: 
                    q.append(node.left) 
                if node.right is not None: 
                    q.append(node.right) 
      
                nodeCount -= 1
