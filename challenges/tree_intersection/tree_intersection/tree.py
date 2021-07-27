
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = value
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def dequeue(self):
        if not self.isEmpty():
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp
        else:
            return ("This Queue are empty, try to fill it first !")
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
    def peek(self):
        try:
            return self.front.value
        except:
            return "This is Empty Queue"
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None




class Tree:
    def __init__(self):
        self.root = None
   

    def breadth_first(self):
        Queue_breadth = Queue()
        output = []
        node = self.root
        Queue_breadth.enqueue(node)
        while Queue_breadth.front:
            node_front = Queue_breadth.dequeue()
            output += [node_front.value]
            if node_front.left:
                Queue_breadth.enqueue(node_front.left)
            if node_front.right:
                Queue_breadth.enqueue(node_front.right)
        return output




class Binary_Search_Tree(Tree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            node = self.root
            while True:
                if node.value >= value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(value)
                        break
                elif node.value < value:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(value)
                        break
 

