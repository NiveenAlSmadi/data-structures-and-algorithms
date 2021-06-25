# Trees
Binary Tree & Binary Search Tree

![image](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/images/BinaryTree1.PNG)


## Challenge
- Binary Tree : 
Create a Binary Tree class
Define a method for each of the depth first traversals:
1- pre order
2- in order
3- post order which returns an array of the values, ordered appropriately.

- Binary Search Tree
Create a Binary Search Tree class ,This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

`Add`
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.

`Contains`
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.
## Approach & Efficiency

O(log(n))

## API
* class Tree :

- `preOrder` : priting the values of the tree by the order of `root >> left >> right`
- `inOrder` : priting the values of the tree by the order of `left >> root >> right`
- `postOrder`: priting the values of the tree by the order of `left >> right >> root`

* class Binary_Search_Tree:

- `Add` : add anode to the tree according to its value
- `Contains` : check if there is a node with tha same value.
