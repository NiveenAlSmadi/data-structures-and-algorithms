from tree_intersection import __version__
from tree_intersection.tree import Binary_Search_Tree
from tree_intersection.code import tree_intersection

def test_version():
    assert __version__ == '0.1.0'


def test_intersection1():
    bst1 = Binary_Search_Tree()
    bst2 = Binary_Search_Tree()
    bst1.add(10)
    bst1.add(12)
    bst1.add(5)
    bst2.add(10)
    bst2.add(5)
    bst2.add(2)
    assert tree_intersection(bst1,bst2) == [10,5]



def test_intersection2():
    bst1 = Binary_Search_Tree()
    bst2 = Binary_Search_Tree()
    bst1.add(1)
    bst1.add(2)
    bst1.add(3)
    bst2.add(3)
    bst2.add(12)
    bst2.add(5)
    assert tree_intersection(bst1,bst2) == [3]



def test_intersection3():
    bst1 = Binary_Search_Tree()
    bst2 = Binary_Search_Tree()
    bst1.add(5)
    bst1.add(20)
    bst1.add(3)
    bst1.add(30)

    bst2.add(3)
    bst2.add(20)
    bst2.add(5)
    bst2.add(17)
    assert tree_intersection(bst1,bst2) == [3,20,5]
