from left_join import __version__
from left_join.code import *


def test_version():
    assert __version__ == '0.1.0'



def test_join_1():
    hash1 = Hashtable(800)
    hash1.add('fond', 'enamored')
    hash1.add('wrath', 'anger')
    hash1.add('diligent', 'employed')
    hash1.add('outfit', 'garb')
    hash1.add('guide', 'usher')
    hash2 = Hashtable(800)
    hash2.add('fond', 'averse')
    hash2.add('wrath', 'delight')
    hash2.add('diligent', 'idle')
    hash2.add('guide', 'follow')
    hash2.add('flow', 'jam')
    assert left_join(hash1, hash2)==[['outfit', 'garb', 'NULL'], ['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow'], ['diligent', 'employed', 'idle']]


def test_join_2():
    hash1 = Hashtable(800)
    hash1.add('a', '1')
    hash1.add('b', '2')
    hash2 = Hashtable(800)
    hash2.add('a', '')
    hash2.add('k', '8')
   
    
    assert left_join(hash1, hash2)==[['b', '2', 'NULL'], ['a', '1', '']]

        
def test_join_3():
    hash1 = Hashtable(800)
    hash1.add('a', '1')
    hash1.add('b', '2')
    hash1.add('z', '1')
    hash1.add('k', '2')
    hash2 = Hashtable(800)
    hash2.add('a', '')
    hash2.add('l', '8')
    hash2.add('y', '7')
    hash2.add('j', '8')
   
    
    assert left_join(hash1, hash2)==[['k', '2', 'NULL'], ['z', '1', 'NULL'],['b', '2', 'NULL'],['a', '1', '']]

