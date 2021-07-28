from left_join.Hashtable import *






def left_join(hash1, hash2):
    result = []
    for item in hash1.map:
        if item:
            hash_value = item.head.value
            if hash2.contains( hash_value[0]):
                result.append([ hash_value[0], hash_value[1],hash2.find( hash_value[0])])
            else:
                result.append([ hash_value[0], hash_value[1],'NULL'])
    return result





if __name__ == '__main__':
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
    print(left_join(hash1, hash2))






