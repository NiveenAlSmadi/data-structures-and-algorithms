class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None



    def push(self, value):
        node = Node(value)
        if self.top == None:
            self.top = node 
        else:
            node.next = self.top
            self.top = node



    def pop(self):
        if not self.isEmpty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            return "This is Empty stack"



    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


    def peek(self):
        try:
            return self.top.value
        except:
            return "This is Empty stack"
            