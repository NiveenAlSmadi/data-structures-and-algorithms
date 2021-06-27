class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None 
        
class Binary_Tree:

    def __init__(self): 
       self.root=None 


    def pre_order(self):
        output=[]
        if not self.root:
            return output
        def traversal(node):
            output.append(node.value)
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)

        traversal(self.root)
        return output


    def in_order(self):
        output=[]
        if not self.root:
            return output

        def traversal(node):
            if node.left:
                traversal(node.left)
            output.append(node.value)
            if node.right:
                traversal(node.right)

        traversal(self.root)
        return output



    def Post_order(self):

        output=[]

        if not self.root:
            return output

        def traversal(node):
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
            output.append(node.value)

        traversal(self.root)
        return output


class Binary_Search_Tree(Binary_Tree):

    def add(self,value):
        if not self.root:
            self.root = Node(value)
            return

        current_node=self.root
        while True:
            if Node(value).value < current_node.value:
                if current_node.left:
                    current_node= current_node.left
                else:
                  current_node.left = Node(value)
                  return 
            else:

                if current_node.right:
                    current_node=current_node.right
                else:
                  current_node.right = Node(value)
                  return

    def contains(self,value):
        if  not self.root:
            return "This is empty tree"

        current_node=self.root  

        while current_node :

            if current_node.value== value:
                return True

            if current_node.value <value: 
                current_node=current_node.right
            else:
                current_node=current_node.left
        return False



    def find_maximum_value(self):

        if  self.root == None:
            return "This is empty tree"

            
        node=self.root
        global max_value
        max_value=node.value
        def maximum(node):
            global max_value
            if not node :
                return max_value

            if node.value>max_value:
                max_value=node.value
            maximum(node.right)
            maximum(node.left)
        maximum(self.root)
        return max_value    




