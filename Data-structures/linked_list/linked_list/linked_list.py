from typing import List


class Node:
    def __init__(self,value):
        self.value= value
        self.next= None


class Linkedlist:
    def __init__(self):
        self.head = None        



    def insert(self, value):
        """
         Adds a node of a value to the head of LL
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
             raise Exception("Sorry, this linkedlist has a head ")


    def includes(self,value):
        """
         Return T/F if value is in the linked list or not
        """
        if self.head:
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False   
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value ")


    def __str__(self):

        # "{ a } -> { b } -> { c } -> NULL"
        # Loop over all nodes
        # print all values in one line
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> ' 
                current = current.next
            data_str += 'NULL'
            return data_str
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value ")


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)        

