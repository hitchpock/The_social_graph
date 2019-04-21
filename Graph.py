from Node import Node

class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)
        #return self.nodes[-1]
    
    def add_list(self, nodes):
        self.nodes.extend(nodes)
 