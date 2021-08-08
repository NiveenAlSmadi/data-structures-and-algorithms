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

def treavers(self,node1,node2):
    if node1==None and node2==None :
      return True 
    if node1 is None or node2 is None :
      return False
    left=self.treavers(node1.left,node2.right)
    right=self.treavers(node1.right,node2.left)
    return(left and right and node1.value==node2.value)

def is_symmetric(self):
    node=self.root
    if node:
      return treavers(node,node)

def maxi(a,b):
  return a if a>b else b
def Height(self,root):
  if root is None :
     return 0
  return 1+ maxi(self.Height(root.right),self.Height(root.left))
```
