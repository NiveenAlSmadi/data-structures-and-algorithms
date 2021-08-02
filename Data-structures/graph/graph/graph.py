from .queue  import *


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



    def breadth_first(self,node):

       breadth=Queue()
       visited=[]
       nodes=[]
       breadth.enqueue(node)
       visited.append(node)
       while breadth.front:
            front=breadth.dequeue()
            nodes.append(front.value)
            for child in self.adjacency_list[front]:
                if child.node not in visited:
                   visited.append(child.node)
                   breadth.enqueue(child.node)
       return nodes         





if __name__=="__main__":
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')

    g.add_Edge(a,b,5)
    g.add_Edge(b,c,4)  
    g.add_Edge(c,a,3)
    g.add_Edge(b,a,1)

    print(g.breadth_first(a))






               