```
from collections import Queue
class Node:
  def __init__(self,value):
    self.value=value
    self.left=None 
    self.right=None 


class Tree:

  def __init__(self):
     self.root=None
  
  def pre_order(self):
    output=[]

    def __walk(node):
       output.append(node.value)
       if node.left:
          __walk(node.left)
       if node.right:
          __walk(node.right)
    __walk(self.root)
    return output


  def in_order(self):
    output=[]

    def __walk(node):
      if node.left:
        __walk(node.left)
      output.append(node.value)
      if node.right:
        __walk(node.right)   
    __walk(self.root)
    return (output)    

  def post_order(self):
      output=[]

      def __walk(node):
        if node.left:
          __walk(node.left)
        if node.right:
          __walk(node.right)
        output.append(node.value)    
      __walk(self.root)  
      return output 

  def bredth_first(self):
    output=[]
    bredth=Queue()
    bredth.enqueue(self.root)
    while bredth.front :
      node=bredth.dequeue()
      output.append(node)
      if node.left:
        bredth.enqueue(node.left)
      if node.right:
        bredth.enqueue(node.right)
    return output       


  def find_maximum(self):
    node=self.root
    global maxval
    maxval=node.value
    def _maxi(node):
        global maxval
        if node.value > maxval:
          maxval=node.value
          _maxi(node.left)
          _maxi(node.right)
    _maxi(self.root)
    return maxval
  



  def find_max(self,root):
      maxval=self.root.value
      left=self.find_max(root.left)
      right=self.find_max(root.right)
      if left >maxval:
        maxval=left
      if right>maxval:
        maxval=right 
      return maxval  



  def add (self,value):
    new_node=Node(value)
    if self.root==None:
      self.root=new_node
    else:
      node=self.root  
      while True:
        if new_node.value<node.value:
          if node.left:
            node=node.left
          else:
            node.left=new_node
            break
        if new_node.value>node.value:
           if node.right:
              node=node.right
           else:
              node.right=new_node
              break

  def contain (self,value,new_val):
    if self.root == None:
         return "empty tree"
    node=self.root
    while node:
      if node.value==value:
        node.value=new_val
      if node.value>value:
             node=node.left
      else:
        node=node.right
    
    return False
  
  def sum (self):
    total=[0]
    def _walk(node):
      total[0]+=node.value
      _walk(node.left)
      _walk(node.right)
    _walk(self.root) 
    return total[0] 
          
            
  def kth_maximum (self,k):
   max_values=[]
   def _walk(node):
     if node :
       _walk(node.left)
       max_values.append(node.value)
       _walk(node.right)  
     _walk(node)
     return max_values[-k]

              
  def kth_minmum (self,k):
   min_values=[]
   def _walk(node):
     if node :
       _walk(node.left)  
       min_values.append(node.value)
       _walk(node.right)
     _walk(node)
     return min_values[k-1]
  
  def delete_leaf(self,value):
    node=self.root
    if node :
      def walk(node):
        if node.left and node.left.value==value:
          node.left=None
        if node.right and node.right.value==value:
          node.right=None 
          walk(node.right) 
          walk(node.left)
      walk(self.root) 

# ------------------------------------------- 

def isSymmetric(root):
    def check(root1,root2):
        if root1 is None and root2 is None:
            return True 
        
        if (root1 is not None and root2 is not None):
            if root1.value == root2.value:
                return (check(root1.left , root2.right) and
                 check(root1.right, root2.left))
            
            return False
    return check(root, root)

def maxi(a,b):
  return a if a>b else b
def Height(self,root):
  if root is None :
     return 0
  return 1+ maxi(self.Height(root.right),self.Height(root.left))
```



```

def max_min(self):
      max=[self.root.value]
      min =[self.root.value]
      node=self.root
      def travers(node):
           if node.value>max[0]:
                max[0]=node.value
           if node.value<min[0]:
                min[0]=node.value
            travers(right)
            travers(left)
       travers(self.root)
       return min[0],max[0]

def is_BST(tree):
    flag=[True]
    node=tree.root
    if node :
        def travers(node):
            if (node.left.value < node.value and
                  node.right.value > node.value ):
                 travers(node.left)
                 travers(node.right)
            else:
               flag[0]=False
         travers(node)
         return flag

def longest_path (root): 
 left_side=[]
 right_sid=[]
 if node is None :
       return [ ]
                  
right_side=[root.value]+longest_path(root.right)

left_side=[root.value]+longest_path(root.left)

return right_side if right_side > left_side else left_side
           

```





