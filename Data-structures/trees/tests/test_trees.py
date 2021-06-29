import pytest
from trees import __version__
from trees.tree import Binary_Tree, Node,Binary_Search_Tree,Queue,k_ary_Node,tree_fizz_buzz,k_ary_tree,tree_fizz_buzz_binary

def test_version():
    assert __version__ == '0.1.0'

#Can successfully instantiate an empty tree
def test_instantiate():
    tree = Binary_Tree()
    assert tree.root == None

#Can successfully instantiate a tree with a single root node
def test_single_root():
    tree = Binary_Search_Tree()
    tree.add('niveen')
    assert tree.root.value == 'niveen'

#Can successfully add a left child and right child to a single root node
def test_add_left_right():
    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(8)
    bst.add(20)
    assert bst.root.value==10
    assert bst.root.left.value==8
    assert bst.root.right.value==20


def test_BinarySearchTree():
    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(12)
    bst.add(5)
    assert bst.pre_order() == [10,5,12]


#Can successfully return a collection from a preorder traversal
def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == ['A','B','D','E','C','F']

#Can successfully return a collection from an inorder traversal
def test_in_order(prepared_tree):
    assert prepared_tree.in_order() == ['D', 'B', 'E', 'A', 'F', 'C']


#Can successfully return a collection from a postorder traversal
def test_Post_order(prepared_tree):
    assert prepared_tree.Post_order() == ['D', 'E', 'B', 'F', 'C', 'A']

#Can successfully cheack a value on tree if contains or not 
def test_contains():
    bst = Binary_Search_Tree()
    bst.add(10)
    assert bst.contains(20) == False
    assert bst.contains(4) == False

#Can successfully return a maximum value on tree 
def test_maximum_value():
    bst =Binary_Search_Tree()
    bst.add(10)
    bst.add(12)
    bst.add(21)
    bst.add(50)
    bst.add(1000)
    bst.add(700)
    assert bst.find_maximum_value()== 1000

 #Can successfully return list of all values in the tree, in the order they were encountered  
def test_breadth_first():
    bt =  Binary_Search_Tree()
    bt.add(10)
    bt.add(12)
    bt.add(21)
    bt.add(50)
    bt.add(1000)
    bt.add(700)
    assert bt.breadth_first()== [10,12,21,50,1000,700]


#Can successfully Determine whether or not the value of each node is divisible by 3, 5 or both 
def test_fuzz_buzz():
    tree = Binary_Tree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(12)
    tree.root.right.left = Node(15)
    expected=['2','7','Buzz','2','Fizz','FizzBuzz']
    actual= tree_fizz_buzz_binary(tree).breadth_first()
    assert expected==actual






def test_k_ary_tree():

    k_tree = k_ary_tree()
    k_tree.root = k_ary_Node(1)
    k_tree.root.child.append(k_ary_Node(22))
    k_tree.root.child.append(k_ary_Node(9))
    k_tree.root.child.append(k_ary_Node(4)) 

    k_tree.root.child[0].child.append(k_ary_Node(5)) 
    k_tree.root.child[0].child[0].child.append(k_ary_Node(10)) 
    k_tree.root.child[0].child.append(k_ary_Node(6)) 
    k_tree.root.child[0].child[1].child.append(k_ary_Node(14))
    k_tree.root.child[0].child[1].child.append(k_ary_Node(12))
    k_tree.root.child[0].child[1].child.append(k_ary_Node(13)) 
    k_tree.root.child[2].child.append(k_ary_Node(15))
    k_tree.root.child[2].child.append(k_ary_Node(25))
    k_tree.root.child[2].child.append(k_ary_Node(9))

    new_tree = tree_fizz_buzz(k_tree)  
    assert new_tree.root.value == '1'      
    assert new_tree.root.child[0].value == '22'
    assert new_tree.root.child[1].value == 'Fizz'
    assert new_tree.root.child[2].value == '4'
    assert new_tree.root.child[0].child[0].value == 'Buzz' 
    assert new_tree.root.child[0].child[0].child[0].value == 'Buzz'
    assert new_tree.root.child[0].child[1].value == 'Fizz'
    assert new_tree.root.child[0].child[1].child[0].value == '14'
    assert new_tree.root.child[0].child[1].child[1].value == 'Fizz'
    assert new_tree.root.child[0].child[1].child[2].value == '13'
    assert k_tree.root.child[2].child[0].value == 'FizzBuzz'
    assert k_tree.root.child[2].child[1].value == 'Buzz'
    assert k_tree.root.child[2].child[2].value == 'Fizz'

@pytest.fixture
def prepared_tree():
    tree = Binary_Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree
