## Introduction

- Trees are used to represent hierarchical data.
- The top most elements of the tree is called *Root*
- An element in a tree is called a *node* 
- *Edges* connect two nodes together to form a *parent-child* relation
- Edges in tree have top to bottom direction
- Nodes that do not have any children are called *Leaf nodes*
- Nodes with same parent are called *Sibling nodes*
- Nodes with same distance from root are called nodes on same level.
	- Root node is at level 0
	- Children to root are at level 1 (one edge apart)
	- Grandchildren to root or nodes that 2 edges apart are at level 2 (And so on...)
- Depth of a node
	- Level at which the node is present
	- Also can be referred as distance from root.
- Height of a node
	- Length of longest path from node to the farthest leaf.
- Height of a tree is the height of root node.
- Nodes at same level are called *Cousin nodes*

![[Pasted image 20240122211546.png]]

## Sub trees

- Any part of tree is called sub tree of that given tree.
- All nodes of the tree nodes should be taken. If we select any node from a tree to form part of sub tree, all its children down to leaf should be taken in.

### How many sub trees are possible for a given tree with N nodes ?
- Since each node can be a possible sub-tree
- Therefor the number possible sub-trees is *N*

## Nomenclature of a tree

- A tree is named according to max number of children a given node can have.

| Max number of children | Name of tree |
|------------------------|--------------|
| 2                      | Binary tree  |
| 3                      | Ternary tree |
| N                      | N-ary tree   |

## Binary tree

- A tree where any node can have at max 2 children i.e. a node may have 0, 1 or 2 children.
- The two children are called `left and right child`

### Structure of binary tree

```java
class Node {
	int data;
	Node left;
	Node right;

	Node(int data) {
		this.data = data;
		this.left = null;
		this.right = null;
	}
}
```

## Traversals of tree

![[Pasted image 20240122224855.png]]

Consider the above tree and perform the below traversal
1. pre-order traversal
2. post-order traversal
3. in-order traversal
4. Level order traversal
5. Vertical traversal
