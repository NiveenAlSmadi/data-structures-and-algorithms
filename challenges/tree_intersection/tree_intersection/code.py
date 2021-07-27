from tree_intersection.tree import Binary_Search_Tree
def tree_intersection(tree1 , tree2):
    tree1 = tree1.breadth_first()
    tree2 = tree2.breadth_first()
    output = list(set(tree1) & set(tree2))
    return output



if __name__ == '__main__':
    bst1 = Binary_Search_Tree()
    bst2 = Binary_Search_Tree()
    bst1.add(30)
    bst1.add(8)
    bst1.add(20)
    bst1.add(10)
    bst2.add(30)
    bst2.add(2)
    bst2.add(8)
    bst2.add(40)
    print (tree_intersection(bst1,bst2))
    
