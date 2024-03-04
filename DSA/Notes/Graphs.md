---
tags:
  - Graphs
date: 4-March-2024
---
```table-of-contents
```
## Introduction

- Collection of nodes and edges.
- Examples
	- Social media => Nodes: Users, Edges: Connections between users
	- Network of computers => Nodes: Computers, Edges: something like latency
	- Google maps: Nodes: Landmark, Edges: roads connecting landmarks

## How to represent ?

- Nodes are represented as numbers
- Example: Node(N) => 1, 2, 3, 4 .. N

![[Graph.png]]

- In case of Facebook, if A is a friend of B, B is also a friend of A. This requires a bi-directional relationship. This kind of relationship is represented by *Undirected graphs*
- In case of Instagram, the relationship is uni-directional (if A follows B does not mean B follows A). These relationships are represented using *Directed graphs.*
- If edges are assigned values, it is defined as *Weighted graphs*. Examples: If we are defining Cost of airline tickets, nodes will be source and destinations and weight will be the cost of ticket like Delhi and Bengaluru are nodes and cost of ticket INR 15K is weight
- *Unweighted graph* is the opposite of weighted graphs.
- So we have 4 types of graphs
	- Undirected unweighted graph
	- Undirected weighted graph
	- Directed unweighted graph
	- Directed weighted graph

### Cyclic vs Acyclic Graphs

![[Cyclic Graphs.png]]

Definition of *Cyclic graph*:

- If it is possible to come back to any node of the graph without repeating an edge
- If a graph contains 1 cycle, it is a cyclic graph

*Acyclic graph:* A graph that is not cyclic is called Acyclic


> [!NOTE] Properties of Graph
> - Directed/Undirected are properties of a graph.
> - Weighted/Unweighted are properties of a graph
> - Being connected is not a property.
> - All properties should be given in a DSA question. 

## In-degree and out-degree

*Degree (of a node)*: Defined as number of adjacent nodes present for a given node.

- In the below graph, degree of node 1 is 2

![[Cyclic Graphs.png]]
*Neighbour of a node*: Nodes at a distance of 1.

*In-Degree*: Number of incoming edges to a node. In degree of 1 is 1

*Out-degree*: No. of outgoing edges to a node. Out degree of 3 is 2

![[Directed Graph.png]]

## Representation of a graph.

![[Pasted image 20240304221956.png]]

Consider the above graph.

*How input is given in a DSA question*

1. No. of Nodes: N
2. No. of edges: E
3. E lines of input where each line represents an edge as (source, destination). In case of weighted graph, it will be (source, destination, weight)

For the above graph, the input will be given as below

```
N=6
E=8
3, 4
3, 5
4, 6
5, 6
2, 1
1, 3
4, 2
2, 5
```

### How to store a graph?

- Two popular ways
	- Adjacency List
	- Adjacency Matrix
- The information that these notations store is information of the neighbours => Thus the name adjacency

### Adjacency matrix

> [!NOTE] What is the max number of nodes for N node graph
> Undirected graph: $n \choose k = n*(n-1)/2$ OR nCr
> Directed graph: $\binom{n}{2} * 2 = n*(n-1)$ OR nCr * 2

- Since both representation are O(n^2), we can can store Adjacency matrix as

$$
	MAT[N][N] = 
		\begin{cases}
		0 &\text{ if edge does not exist} \\
		1 &\text{ if edge does exit}
		\end{cases}
$$

- For the above example we need a matrix of size `7*7` because we have 1 based indexing.

| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |

```java
int[][] buildAjdmatrix(int V, int[] E) {
	int[][] matrix = new int[V+1][V+1];

	for (int i=0; i<E.size(); i++) {
		int source = E[i][0];
		int desitnation = E[i][1];
		matrix[source][desitination] = 1;
	}
	return matrix;
}
```

**Complexity analysis**
Time complexity: O(n^2) => Fill matrix with value zero as well
Space complexity: O(n^2)

**Advantages of adjacency matrix**
1. Random access = Constant time to access a node
2. Constant time to add a node.
3. Constant time to remove a node.

**Disadvantages of adjacency matrix**
1. Not space optimal
2. Find neighbours is not constant.