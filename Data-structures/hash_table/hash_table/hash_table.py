from hash_table.linked_list import Linkedlist


class Hash_table:

    def __init__(self,size):
        self.size=size
        self.map=[None]*size

    def add(self, key, value):
       hashed_key = self.Gethash(key)
        
       if not self.map[hashed_key]:
            self.map[hashed_key] = Linkedlist()
       self.map[hashed_key].add((key,value))

    def get(self,key):
        hashed_key=self.Gethash(key)
        if self.map[hashed_key]:
            return self.map[hashed_key].get(key)[1]
        return 'NULL'    
        
    def contains(self,key):
        hashed_key=self.Gethash(key)
        if self.map[hashed_key]:
        
            return self.map[hashed_key].includes(key )
        return False

    def Gethash(self,key):
        
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 17
        hashed_key = temp_value % self.size
        return hashed_key



if __name__ == '__main__':
    hashtable = Hash_table(1024)
    hashtable.add('niveen', 22)
    hashtable.add('niv', 21)
    hashtable.add('silent', True)
    hashtable.add('listen', 'Hey man')
    hashtable.add('class', 'Python-401d4')
    val= hashtable.contains('niv') 
    for index, item in enumerate(hashtable.map):
        if item:
            print(index, item)  
   