#  @details All search methods in this module assume that node1 and node2 are different

from collections import deque

# Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

# Breadth First Search
# Return path between node1 and node2
def BFS2(G, node1, node2):
    Q = deque([[node1]])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_path = Q.popleft()
        current_end = current_path[-1]
        for node in G.adj[current_end]:
            if node == node2:
                return current_path + [node]
            if not marked[node]:
                Q.append(current_path + [node])
                marked[node] = True
    return []

# Depth First Search
# Return path between node1 and node2
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if node == node2:
                    return [node1] + __history(pred, node1, current_node) + [node2]
                if not marked[node]:
                    S.append(node)
                    pred[node] = current_node
    return []

# Turns the predecessor dictionary into a list of history
def __history(pred_dict, node1, node2):
    if not bool(pred_dict):
        return []
    L = []
    current_node = node2
    while current_node != node1:
        L.append(current_node)
        current_node = pred_dict[current_node]
    return L[::-1] # reverse the list

# Breadth First Search from node1
# Return predecessor dictionary
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    pred = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred[node] = current_node
    return pred

# Depth First Search from node1
# Return predecessor dictionary
def DFS3(G, node1):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            print("Visiting: " + str(current_node))
            for node in G.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    pred[node] = current_node
    return pred

# Helper function for has_cycle and is_connected
def __get_unvisited(marked):
    for node in marked:
        if not marked[node]:
            return node
    return None

# Reused code for has_cycle.
def __BFS4(G, node1, marked):
    Q = deque([node1])
    marked[node1] = True
    pred = {}
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred[node] = current_node
            elif node != pred[current_node]:
                return marked, True
    return marked, False

# Reused code for is_connected.
def __BFS5(G, node1, marked):
    Q = deque([node1])
    marked[node1] = True
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return marked

def has_cycle(G):
    marked={}
    for node in G.adj:
        marked[node] = False
    cycle_found = False
    node = __get_unvisited(marked)
    while node != None and not cycle_found:
        marked, cycle_found = __BFS4(G, node, marked)
        if cycle_found:
            return True
        node = __get_unvisited(marked)
    return False

def is_connected(G):
    marked={}
    for node in G.adj:
        marked[node] = False
    marked = __BFS5(G, __get_unvisited(marked), marked)
    if __get_unvisited(marked) == None:
        return True
    else:
        return False
