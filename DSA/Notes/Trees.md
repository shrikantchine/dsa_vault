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

### Level order traversal

Order = Nodes at each level from left to right
Solution for the above tree = `[10, 5, 15, 3, 8, 12, 18]`

```java
void levelOrder(Node root) {
	if (root == null) return;
	
	Deque<Node> q = new LinkedList<>();
	q.addLast(root);

	while (!q.isEmpty()) {
		Node n = q.removeFirst();
		System.out.println(n.val);
		if (n.left != null) q.addLast(n.left);
		if (n.right != null) q.addLast(n.right);
	}
}
```

### Left View of the tree

- To print left view of the tree, only print the first element in level order

> [!NOTE] Very important
> During each iteration of level order traversal, the initial size of the queue is number of nodes in previous level/

```java
void leftView(Node root) {
	if (root == null) return;
	
	Deque<Node> q = new LinkedList<>();
	q.addLast(root);

	while (!q.isEmpty()) {
		int levelSize = q.size();
		for (int i=1; i<=levelsize; i++) {
			Node n = q.removeFirst();
			if (i == 1) System.out.println(n.val);
			if (n.left != null) q.addLast(n.left);
			if (n.right != null) q.addLast(n.right);
		}
		
	}
}
```

- Similarly right view can be printed by printing the last element using the condition
	`i == levelSize`

### Vertical order traversal

![[Pasted image 20240211220717.png]]

- Lets define "Vertical Index" as
	- Root Node has Vertical index = 0
	- If a node has Vertical Index as `x`, its left node has Vertical Index = `x-1` and right node has Vertical Index as `x+1`
- To Solve for vertical node, we need to define a pair class as
```java
class Pair {
	Node node;
	int vl; // Defines vertical index

	Pair(Node node, int vl) {
		this.node = node;
		this.vl = vl;
	}
}
```

- Now we need some traversal to navigate the tree.
	- Any recursion based traversal will not work since the recursion will print lower nodes before the one's on top. In the above example - Node 15 will be printed before Node 9.
	- Level order traversal is suitable because it always prints the lower levels after upper levels by default.
- We can use a HashMap to store the nodes at a certain vertical index

```java
void verticalOrder(Node root) {
	Deque<Pair> q = new LinkedList<>();
	Pair rootPair = new Pair(root, 0);
	HashMap<Integer, ArrayList<Node>> map = new HashMap<>();
	int min = 0, max = 0;
	q.addLast(rootPair);

	while (!q.isEmpty()) {
		Pair p = q.removeFirst();
		min = Math.min(min, p.vl);
		max = Math.max(max, p.vl);

		if (!map.containsKey(p.val)) {
			map.put(p.val, new ArrayList<>());
		}
		map.get(p.val).add(p.node);
		if (p.node.left != null) q.addLast(new Pair(p.node.left, p.vl-1));
		if (p.node.right != null) q.addLast(new Pair(p.node.right, p.vl+1));
	}

	for (int i=min; i<=max; i++) {
		List<Integer> vlList = map.get(i).stream().map(n -> n.data).toList();
		System.out.println(vlList);
	}
}
```


### Types of Binary trees

#### Proper/Full Binary tree
- Each node has 0 or 2 children
![[Pasted image 20240211223720.png]]

#### Complete Binary tree
- All level should be completely filled except the last level
- In the last level, nodes should be filled from left to right
![[Pasted image 20240211223753.png]]

#### Perfect Binary tree
- All levels are completely filled![[Pasted image 20240211223818.png]]
- Perfect binary tree is also a complete binary tree
- Perfect binary tree is also a perfect binary tree
![[Pasted image 20240211223818.png]]
### Height of a binary tree

- Height of binary tree is defined as "Minimum distance between root node and left node".
- Distance can be defined in terms of edges 
	- Distance is number of edges between root and leaf
	- For the recursion, null node distance is -1
- Distance can be defined in terms of nodes 
	- Distance is number of nodes between root and leaf
	- For the recursion, null node distance is 0

```java
int height(Node root) {
	if (root == null) return -1;
	int lh = height(root.left);
	int rh = height(root.right);
	return Math.max(lh, lr)+1;
}
```


### Balanced Binary tree

- Defined as a binary tree where for all nodes difference between left and right sub tree is less than or equal to 1
- Mathematically

$\forall nodes:  \lvert HeightOfLeftSubTree-HeightOrRightSubtree \rvert <= 1$

**Brute force solution**
```java
boolean isHeightBalanced(Node root) {
	if (root == null) return true;
	int lh = height(root.left);
	int lr = height(root.right);

	if (Math.abs(lh-lr) > 1) return false;
	return isHeightBalanced(root.left) && isHeightBalanced(root.right);
}
```

**Complexity analysis**
- Since height is used as a sub function, same node is revisited again and again
- Time complexity: O(n^2)
- Space complexity: O(n)

**Optimised solution**
- Use a Pair class to pass the information from  lower nodes to upper nodes in the height function

```java
class Pair {
	boolean isBalanced;
	int height;

	// All arg
}
```