class Node:
    def __init__(self,value):

        self.value= value
        self.next= None


class Linkedlist:

    def __init__(self):
        self.head = None        

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

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
                if current.value[0] == value:
                    return True
                current = current.next
            return False   
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value ")
    

    def get(self,value):
        """
        Return the value of key 
        """

        if self.head:
            current =self.head
            while current:
                if current.value[0] == value:
                    return current.value
                current = current.next
            
        else:
            raise Exception("Sorry, this key not found ")




    def __str__(self):

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