class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Stack:



    def __init__(self):
        self.top=None

    def push(self,value):
        node = Node(value)

        if self.top:
          node.next = self.top
          self.top = node
        else :
            self.top=node 

    def pop(self):

        try:
            deleted_value= self.top.value
            temp=self.top.next
            self.top=temp
            temp.next=None
            return deleted_value
        except:
            return "This is Empty stack"



    def peek(self):
        try:
            return self.top.value
        except:
            return "This is Empty stack"




    def isEmpty (self):
        if self.top == None :
            return False
        else:
            return True    

#___________________________________________________________Queune__________________________________________________________________#

class Queue():

    def __init__(self):
        self.front=None
        self.rear=None



    def enqueue(self , value):
        node=Node(value)
        if self.front ==None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node    
            self.rear=node


    def dequeue(self):
        
        try:
            self.front.value

        except:
            return "This is Empty queue"
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
            return temp.value





    def peek(self):
        try:
            return self.front.value
        except:
            return "This is Empty queue"


    def isEmpty (self):

        if self.front == None and self.rear == None :
            return True
        else:
            return False  
        

