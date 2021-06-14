import pytest
from linked_list import __version__
from linked_list.linked_list import Linkedlist , Node



def test_version():
    assert __version__ == '0.1.0'



def test_instantiate():
    List = Linkedlist()
    actual = List.head
    expected = None
    assert actual == expected


def test_insert():
    List = Linkedlist()
    List.insert(6)
    actual=List.head.value
    expected=6
    assert actual == expected



def test_head():
    List = Linkedlist()
    List.insert(10)
    assert List.head.value == 10


def test_find_value():
    List = Linkedlist()
    List.insert(1)
    List.append(5)
    List.append(10)
    assert List.includes(10) == True



def test_find_notExist_value():
    List = Linkedlist()
    List.insert(1)
    List.append(5)
    List.append(10)
    assert List.includes(4) == False



def test_str():
   List = Linkedlist()
   List.insert(1)
   List.append(2)
   List.append(3)
   assert List.__str__()=='{1}-> {2}-> {3}-> NULL'

def test_append():
    actual=''
    List = Linkedlist()
    List.insert(18)
    List.append(6)
    List.append(3)
    while List.head:
       actual+=f'{List.head.value},'
       List.head=List.head.next
    expected='18,6,3,'
    assert actual == expected




#------------------------------------------------------------------------#
def lists():
    List = Linkedlist()
    List.insert(1)
    List.append(2)
    List.append(3)
    List.append(4)
    List.append(5)
    List.append(6)   
    return List                           





def test_inseartBefor():
    List=lists()
    List.insertBefore(2,22)
    List.insertBefore(3,42)
    List.insertBefore(6,18)
    actual=List.__str__()
    expected='{1}-> {22}-> {2}-> {42}-> {3}-> {4}-> {5}-> {18}-> {6}-> NULL'
    assert actual == expected




def test_inseartAfter():
    List=lists()
    List.insertAfter(2,22)
    List.insertAfter(3,42)
    List.insertAfter(6,72)
    actual=List.__str__()
    expected='{1}-> {2}-> {22}-> {3}-> {42}-> {4}-> {5}-> {6}-> {72}-> NULL'
    assert actual == expected


def test_kth_from_end():
    List=lists()
    List.kthFromEnd(0)
    actual=List.kthFromEnd(0)
    expected=6
    assert actual == expected

def test_kth_from_end1():
    List=lists()
    List.kthFromEnd(3)
    actual=List.kthFromEnd(3)
    expected=3
    assert actual == expected


