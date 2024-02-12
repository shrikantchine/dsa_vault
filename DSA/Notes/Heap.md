```table-of-contents
```

## Understanding the use case

### Rope connecting

**Problem statement**
Given an array of integers representing the length of ropes , In one step you can connect two ropes.
Find min steps to connect all nodes.
Cost of connecting two nodes is sum of lengths of two ropes

**Example**
A = [2, 5, 3, 2, 6]
After connecting first two nodes => Array: [7, 3, 2, 6] Cost: 7
After connecting first two nodes => Array: [10, 2, 6] Cost: 17
After connecting first two nodes => Array: [12, 6] Cost: 29
After connecting first two nodes => Array: [18] Cost: 47

**Observations**
- The order in which we pick the rope, the cost will vary.
- If at each step, we take the two smallest ropes, the cost will minimise because 

```text
Given 3 ropes: x, y, z where length has relation x < y < z

		   Way 1      Way 2      Way 3
Step 1 :   x+y        x+z        y+z
Step 2 :   (x+y)+z    (x+z)+y    (y+z)+x

Since the step 2 is same for all ways, we need to minimise Step 1. This means cost of last step is always same for all options but to minimise the cost of previous steps, we need to choose the least two lengths
```

- Sorting and adding will not work because if we sort and keep adding, the first element may not be smallest element anymore
	- Solution: After every addition, position the first element correctly which requires time complexity o(n^2)
	- For example, try the above example
- What is required ?
	- Get Min and second min
	- Insert a new element after every step.
- *Heap* is the data structure that can help and provide both operation in *O(log n)*

### Heap

- Heap is a complete binary tree => all levels are filled except the last level which is filled from left to right.
- There are two types of Heap
	- Min Heap
	- Max Heap
- *Heap order property (Defined for min Heap):* 
	$\forall nodes: node.data <= node.left.data \space AND \space node.data <= node.right.data$
- Similarly we can defined the heap order property for max Heap
	$\forall nodes: node.data >= node.left.data \space AND \space node.data >= node.right.data$


> [!NOTE] Relation between heap nodes
> In a heap, there is no relation between left and right nodes. The only relation is what is defined above.

### Serialise a binary tree

- For complete binary trees, level order traversal can be considered.
- From an array we can figure out the left nodes as below


> [!NOTE] How to navigate in serialised array
>Given a node at array index `i` => Left node is at `2i + 1` & right node is at `2i+2`
> Given a node at array index `i` => Parent node is at `(i-1)/2`

## How to insert a new node to Heap

- Insert at the end of the array
- Perform *Up Heapify*
	- Get the parent
	- If parent is not following heap order property, swap the data between the current node and parent node. 
	- Repeat till the root node or the heap property is already maintained at parent node.

```java
void upHeapify(int[] heap, int index) {
	int parent = (index-1)/2;

	while (index != 0 && heap[parent] > heap[index]) {
		int tmp = heap[parent];
		heap[parent] = heap[index];
		heap[index] = tmp;
		index = parent;
		parent = (index-1)/2;
	}
}
```