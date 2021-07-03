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

    # following sedgwik: h = self, x = self.right
    # def rotate_right(self):
    #     h = self
    #     x = self.left
    #     self.left = x.right
    #     if x.right != None:
    #         x.right.parent = x

    #     x.parent = h.parent
    #     if h.parent == None:
    #         self.root = x
    #     elif h == h.parent.right:
    #         h.parent.right = x
    #     else:
    #         h.parent.left = x
    #     x.right = h
    #     h.parent = x

    # def rotate_left(self):
    #     h = self
    #     x = self.right
    #     self.right = x.left
    #     if x.left != None:
    #         x.left.parent = x

    #     x.parent = h.parent
    #     if h.parent == None:
    #         self.root = x
    #     elif h == h.parent.left:
    #         h.parent.left = x
    #     else:
    #         h.parent.right = x
    #     x.left = h
    #     h.parent = x

                      
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
     
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None: #//self is root
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
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None: #//self is root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: #// self is right child
            x.parent.right = y
        y.left = x
        x.parent = y

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
        
    # recursive function
    # explicit return for clearity
    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        
        # if root, make black
        if node.parent == None:
            node.make_black()
            return
        
        # if not root and parent black, no need to fix
        elif node.parent.is_black():
            return
        
        # if not root and parent not black, do the following
        else:
            # uncle black or uncle is null
            if node.uncle_is_black():
                if node.parent.is_left_child() and node.is_left_child():
                    self.__llcase(node)
                    return
                if node.parent.is_left_child() and node.is_right_child():
                    self.__lrcase(node)
                    return
                if node.parent.is_right_child() and node.is_right_child():
                    self.__rrcase(node)
                    return
                if node.parent.is_right_child() and node.is_left_child():
                    self.__rlcase(node)
                    return
            # uncle red
            else:
                node.parent.make_black()
                node.get_uncle().make_black()
                node.parent.parent.make_red()
                self.fix(node.parent.parent)
                return        
            
    def __llcase(self, node):
        self.rotate_right(node.parent.parent)
        node.get_brother().colour, node.parent.colour = \
            node.parent.colour, node.get_brother().colour
        
    def __lrcase(self, node):
        self.rotate_left(node.parent)
        self.__llcase(node.left)
        
    def __rrcase(self, node):
        self.rotate_left(node.parent.parent)
        node.get_brother().colour, node.parent.colour = \
            node.parent.colour, node.get_brother().colour
        
    def __rlcase(self, node):
        self.rotate_right(node.parent)
        self.__rrcase(node.right)
                
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

# test
rbtree = RBTree()
for i in range(1, 10):
    print("Insert: ", i)
    rbtree.insert(i)
    print(rbtree)
    print()














