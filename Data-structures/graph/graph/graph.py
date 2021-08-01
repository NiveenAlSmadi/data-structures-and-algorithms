class Node():
    def __init__(self,value):
        self.value=value


class Edge():
    def __init__(self,node,weight=None):
        self.node=node
        self.weight=weight

class Graphs():

    def __init__(self):
       self.adjacency_list = {}

    def add_node(self,value):
        node=Node(value)
        self.adjacency_list[node] = []
        return node

    def add_Edge(self,node1,node2,weight=None):
      if node1 and node2 in self.adjacency_list:
         self.adjacency_list[node1].append(Edge(node2,weight))
   
    def get_nodes(self):
        if self.adjacency_list.keys():
            return self.adjacency_list.keys()
        else :
            return 'NULL'  

    def get_neighbors(self,node):
        return self.adjacency_list[node]

    def size(self):
        return len(self.adjacency_list) 
        
               