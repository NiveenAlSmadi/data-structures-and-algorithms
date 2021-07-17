from hash_table import __version__
from hash_table.hash_table import Hash_table,Linkedlist
def test_version():
    assert __version__ == '0.1.0'

#Adding a key/value to your hashtable results in the value being in the data structure

def test_add():
   table=Hash_table(10)
   table.add('niveen',"candy")
   assert table.map[table.Gethash('niveen')].head.value==("niveen",'candy')

#Retrieving based on a key returns the value stored

def test_get_value_from_key():
   table=Hash_table(10)
   table.add('sarah',"cookies")
   assert table.get('sarah')=="cookies"

#Successfully returns null for a key that does not exist in the hashtable

def test_key_not_exist():
   table=Hash_table(10)
   assert table.get('leen')=='NULL'

#Successfully handle a collision within the hashtable

def test_handle_collision():
   table=Hash_table(10)
   table.add('reema',"casterd")
   table.add('meera',"Bounty cake")
   assert table.map[table.Gethash('reema')].head.value==("reema",'casterd')
   assert table.map[table.Gethash('meera')].head.next.value==("meera",'Bounty cake')


#Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_retrieve_collision_values():
   table=Hash_table(10)
   table.add('reema',"casterd")
   table.add('meera',"Bounty cake")
   assert table.get('reema')=='casterd'
   assert table.get('meera')=='Bounty cake'


#Successfully hash a key to an in-range value
def test_hash_in_range():
   table=Hash_table(4)
   table.add('niveen',"candy")
   table.add('reema',"casterd")

   assert table.Gethash('niveen')<=4
   assert table.Gethash('reema')==2
  