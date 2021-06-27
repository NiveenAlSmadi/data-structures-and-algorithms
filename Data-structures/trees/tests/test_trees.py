import pytest
from trees import __version__
from trees.tree import Binary_Tree, Node,Binary_Search_Tree

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
    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(12)
    bst.add(21)
    bst.add(50)
    bst.add(1000)
    bst.add(700)
    assert bst.find_maximum_value()== 1000


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
