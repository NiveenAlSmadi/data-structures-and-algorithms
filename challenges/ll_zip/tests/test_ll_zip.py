
from ll_zip.linked_list import Linkedlist
from ll_zip.ll_zip import zip_lists
from ll_zip import __version__


def test_version():
    assert __version__ == '0.1.0'



def test_equal():
    test1 = Linkedlist()
    test2 = Linkedlist()
    test1.append(10)
    test1.append(30)
    test1.append(20)
    test2.append(50)
    test2.append(90)
    test2.append(40)
    zip_lists(test1,test2)
    expected = "{ 10 } -> { 50 } -> { 30 } -> { 90 } -> { 20 } -> { 4 0} -> { Null } -> "
    actual = test1.__str__()
    assert expected == actual

def test_not_equal():
    test1 = Linkedlist()
    test2 = Linkedlist()
    test1.append(11)
    test1.append(33)
    test2.append(50)
    test2.append(90)
    test2.append(40)
    zip_lists(test1,test2)
    expected = "{ 11 } -> { 50 } -> { 30 } -> { 90 } -> { 40 } -> { Null } -> "
    actual = test1.__str__()
    assert expected == actual

def test_not_equal2():
    test1 = Linkedlist()
    test2 = Linkedlist()
    test1.append(12)
    test1.append(32)
    test1.append(22)
    test2.append(52)
    test2.append(92)
    zip_lists(test1,test2)
    expected = "{ 12 } -> { 52 } -> { 32 } -> { 92 } -> { 22 } -> { Null } -> "
    actual = test1.__str__()
    assert expected == actual