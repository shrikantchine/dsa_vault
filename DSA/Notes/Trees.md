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

![[Pasted image 20240122225853.png]]

Consider the above tree and perform the below traversal
1. pre-order traversal => Node, Left child,  Right
2. post-order traversal => Left, Node, Right
3. in-order traversal => Left, Right, Node
4. Level order traversal
5. Vertical traversal


### Pre-order traversal

Order = Node, Left child,  Right
Solution for the above tree => `[10, 5, 3, 8, 15, 12, 18]`

```java
void preOrder(Node root) {
	if (root == null) return;
	System.out.println(root.data);
	preOrder(root.left);
	preOrder(root.right);
}
```
**Complexity**
Time complexity of recursion = (Number of recursive calls) * (Time taken per call)
So, time complexity: N calls of O(1) => O(N)
Space complexity: O(N)

### In-order traversal

Order = Left, Node,  Right
Solution for the above tree => `[3, 5, 8, 10, 12, 15, 18]`

```java
void inOrder(Node root) {
	if (root == null) return;	
	inOrder(root.left);
	System.out.println(root.data);
	inOrder(root.right);
}

void inOrderIterative1(Node root) {
	Deque<Node> st = new ArrayDeque<>();
	Node curr = root;

	while (curr != null || !st.isEmpty()) {
		if (curr != null) {
			st.push(curr);
			curr = curr.left;
		} else {
			curr = st.pop();
			System.out.println(curr.data);
			curr = curr.right;
		}
	}
}

void inOrderIterative2(Node root) {
	Deque<Node> st = new ArrayDeque<>();
	if (root != null) {
		st.push(root);
	}

	while (!st.isEmpty()) {
		Node n = st.peek();
		while (n.left != null) {
			st.push(n);
			n = n.left;
		}
		n = st.pop();
		System.out.println(n);
		if (n.right != null) {
			st.push(n.right);
		}
	}
	
}
```
**Complexity**
So, time complexity: O(N)
Space complexity: O(N)

### Post-order traversal

Order = Left,  Right, Node
Solution for the above tree => `[3, 8, 5, 12, 18, 15, 10]`

```java
void postOrder(Node root) {
	if (root == null) return;	
	postOrder(root.left);
	postOrder(root.right);
	System.out.println(root.data);
}
```
**Complexity**
So, time complexity: O(N)
Space complexity: O(N)