from merge_sort.code import merge_sort
from merge_sort import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_sort_arr1():
    arr=[8,4,23,42,16,15]
    actual=merge_sort(arr)
    expected=[4,8,15,16,23,42]
    assert actual==expected


def test_sort_arr2():
    arr=[20,18,12,8,5,-2]
    actual=merge_sort(arr)
    expected=[-2,5,8,12,18,20]
    assert actual==expected

    
def test_sort_arr3():
    arr=[2,3,5,7,13,11]
    actual=merge_sort(arr)
    expected=[2,3,5,7,11,13]
    assert actual==expected    

def test_sort_arr4():
    arr=[5,12,7,5,5,7]
    actual=merge_sort(arr)
    expected=[5,5,5,7,7,12]
    assert actual==expected 
    
           