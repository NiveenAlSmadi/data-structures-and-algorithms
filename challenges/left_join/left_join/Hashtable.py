
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'its a node with value :{self.value} and pointing for : {self.next}'


class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            raise Exception(f"This list already has a head! , try '.append({value})'")



    def includes(self, checkvalue):
        """
        Adds a node of a value to the head of LinkedList
        """
        if self.head != None:
            nodes_values = self.head
            while (nodes_values):
                if nodes_values.value[0] == checkvalue:
                    return True
                nodes_values = nodes_values.next
            return False
        else:
            raise Exception("This list is empty! ,try to insert valus frist")


    def return_value(self, value):
            if self.head != None:
                nodes_values = self.head
                while (nodes_values):
                    if nodes_values.value[0] == value:
                        return nodes_values.value[1]
                    nodes_values = nodes_values.next
                return f"there is no key: {value}"



    def __str__(self):
        if self.head :
            nodes_values = self.head
            string = f''
            while (nodes_values):
                string += '{'+str(nodes_values.value)+'}->'
                nodes_values = nodes_values.next
            return string + "NULL"
        else:
            raise Exception("This list is empty! , nothing to print")


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)


   
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size 



    def get_hash(self, key):
        sum_of_asccii = 0
        for char in key:
            asccii_of_ch = ord(char)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 599
        hashed_key = temp_value % self.size
        return hashed_key



        
    def add(self, key, value):
        hashed_key = self.get_hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].append((key,value))




    def contains(self,key):
        hashed_key=self.get_hash(key)
        if self.map[hashed_key]:
            return self.map[hashed_key].includes(key)
        return False   




        
    def find(self, key):
        hashed_key=self.get_hash(key) 
        if self.map[hashed_key]:
           return self.map[hashed_key].return_value(key) 
        else:
            return None            
