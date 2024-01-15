## Introduction

Linked List is a non-continuous linear data structure. Below are the advantages

1. Compared to arrays, it does not have a restriction of being continuous. So even in low continuous memory situations, linked list can be instantiated.
2. Compared to dynamic arrays, it only uses only the required space. In contrast dynamic arrays double their size which might result in unused space being allocated.

## Commonly used approaches in Linked List

### Previous and Current pointers
- Define two pointers `prev = null` & `curr = head`
- At each iteration
	- `prev` pointer moves to `curr` pointer
	- `curr` pointer moves 1 step ahead.
- This approach allows us to keep track of previous pointer in case we need to access it later 
> Look at the "Insert / Delete in a Linked list"

### Slow and Fast pointer approach
- Define two pointers `slow` & `fast`
- At each iteration 
	- `slow` pointer moves 1 step.
	- `fast` pointer moves 2 steps.
- This approach allows us to find the MID element of Linked list in 1 iteration.

> Look at the question "Find MID element" below
## How to define ?

- Data is stored in *Node*
- The first node is referenced by the variable *head*
- Each node stores the address of next node
- Example Node definition

```java
class Node {
	int data;
	Node next;

	Node(int data) {
		this.data;
		next = null;
	}

	@Override  
	public String toString() {  
	    String x = String.valueOf(data);  
	    if (next == null) return x;  
	    return x + " -> " + next;  
	}
}
```

- Example linked list
```java
Node head = new Node(10);
Node n1 = new Node(15);
Node n2 = new Node(5);
Node n3 = new Node(20);

head.next = n1;
n1.next = n2;
n2.next = n3;

// This results in below linked list
```

![[Pasted image 20240110213004.png]]

### Create linked list from array

**Problem statement**
Given an array of size N (>= 1), create a linked list and return its head.

**Solution**
```java
Node createLinkedList(int[] arr) {
	Node head = new Node(arr[0]);
	Node current = head;

	for (int i=1; i<arr.length; i++) {
		Node n = new Node(arr[i]);
		current.next = n;
		current.next;
	}

	return head;
}
```

### Element in Kth index (0 based)

**Problem statement** 
Given the head of the linked list, return the element on kth index

**Solution**
```java
int kthElement(Node head, int k) {
	int i=1;
	Node current = head;
	while (current != null && i++ <= k) current = current.next;
	return current == null ? -1 : current.data;
}
```

### Check if element is present

**Problem statement**
Given a linked list, Check if an element is present in the linked list

**Solution**
```java
boolean contains(Node head, int k) {
	Node current = head;
	while (current != null) {
		if (current.data == k) return true;
		current = current.next;
	}
	return false;
}
```

**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)

### Size of linked list

**Problem statement**
Given a linked list, return its size

**Solution**
```java
int size(Node head) {
	Node current = head;
	int result = 0;
	while (current != null) {
		result++;
		current = current.next;
	}
	return result;
}
```

**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)

### Insert Node

**Problem statement**
Given a linked list, insert a new node given data K at the index P. Also return the head of the updated linked list.

**Solution**
```java
Node insert(Node head, int k, int p) {
	Node newNode = new Node(k);
	if (p == 0) {
		newNode.next = head;
		head = newNode;
		return head;
	}
	Node curr = head;
	int i=0;
	while (curr != null && (i < p-1)) {
		curr = curr.next;
		i++;
	}
	if (curr == null) {
		throw new IllegalStateException("Not possible to insert");
	}

	newNode.next = curr.next;
	curr.next = newNode;

	return head;
}
```

**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)

### Delete an element

**Problem Statement**
Given a linked list, delete the first occurrence of element K. Return the head of updated linked list.

**Solution**
```java
Node delete(Node head, int k) {
	if (head == null) return null;
	if (head.data == k) return head.next;
	
	Node curr = head, prev = null;
	while (curr != null) {
		if (curr.data == k) {
			prev.next = curr.next;
			break;
		}
		prev = curr;
		curr = curr.next;
	}

	return head;
}
```

**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)

### Reverse a linked list

**Problem statement**
Given a linked list, reverse it and return the head of reversed linked list.

**Solution**
```java
Node reverse(Node head) {
	Node curr = head, prev = null;

	while (curr != null) {
		Node tmp = prev;
		prev = curr;
		curr = curr.next;
		prev.next = tmp;
	}

	return prev;
}
```

**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)

### Check if linked list is palindrome

**Problem statement**
Given a linked list, return true if it is a palindrome otherwise return false.

**Solution 1**

1. Make a copy of linked list
2. Reverse a linked list
3. Compare both linked list
**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)

**Solution 2**
1. Break the second half
2. Reverse the second half
3. Compare both halves

```java
public boolean lPalin(ListNode A) {
	if (A == null) return false;
	if (A.next == null) return true;
	ListNode slow = A, fast = A;
	while (fast != null && fast.next != null && fast.next.next != null) {
		fast = fast.next.next;
		slow = slow.next;
	}
	
	ListNode right = slow.next;
	slow.next = null;	
	ListNode reversed = reverse(right);
	ListNode p1 = A, p2 = reversed;
	while (p1 != null && p2 != null) {
		if (p1.val != p2.val) return false;
		p1 = p1.next;
		p2 = p2.next;
	}
	slow.next = reverse(right);
	return true;
}
```

### Find MID of a linked list

**Problem statement**
Given a linked list, find the middle element.
- For odd length, the mid element is `(N/2)+1`
- For even length, the mid is `N/2`

**Solution (Slow and fast pointer approach)**
```java
Node getMiddle(Node head) {
	if (head == null) return null;
	Node slow = head, fast = head;
	while (fast.next != null && fast.next.next != null) {
		fast = fast.next.next;
		slow = slow.next;
	}
	return slow;
}
```

**Complexity**
Time complexity: O(n) where n is length of linked list
Space complexity: O(1)
- Even though the time complexity is O(n), we are using only 1 iteration, which is not possible if we find the length of Linked List and find element at mid index

### Merge two sorted linked list

**Problem statement**
Given two sorted linked list, merge them in a sorted order and return the head of merged linked

**Solution**
```java
Node merge(Node head1, Node head2) {
	if (head1 == null) return head2;
	if (head2 == null) return head1;

	Node head = new Node(-1);
	Node curr = head;

	while (head1 != null || head2 != null) {
		if (head1.data < head2.data) {
			curr.next = head1;
			head1 = head1.next;
		} else {
			curr.next = head2;
			head2 = head2.next;
		}
		curr = curr.next;
	}

	if (head1 != null) curr.next = head1;
	if (head2 != null) curr.next = head2;

	return head.next;
}
```

**Complexity**
Time complexity: `O(n1 + n2) ` where `n1` and `n2` are lengths of given linked lists
Space complexity: O(1)

### Merge sort on Linked List

**Problem sort**
Given a linked list, sort it using merge sort

**Solution**
```java
Node mergeSort(Node head) {
	if (head == null || head.next == null) return head;

	Node mid = getMiddle(head);
	Node h2 = mid.next;
	mid.next = null;
	Node h1 = mergeSort(head);
	h2 = mergeSort(h2);
	return merge(h1, h2);
}
```

**Complexity**
- Time complexity  of `getMiddle` is `O(n)`
- Time complexity of `merge` is `O(n)`
- Time complexity of recursion `O(log n)`
- Therefore, total time complexity `O(n log n)`

- Space complexity: Recursion stack space uses `O(log n)`

## Circular linked list

- Circular list is one where last/tail node points back to head of the list
- Circular list cannot have any node pointing to null.
- How to figure out if linked list is circular ?
	- While iterating check `head == current`

![[Pasted image 20240112223932.png]]

## Linked list with a cycle

- Tail node of the linked list points to any node of the linked list.

![[Pasted image 20240112224038.png]]


### Detect cycle in a linked list

**Problem statement**
Given a linked list, check if it contains a cycle.

**Solution**
```java
public boolean hasCycle(ListNode head) {

	if (head == null || head.next == null) return false;
	ListNode slow = head, fast = head;
	
	while (fast.next != null && fast.next.next != null) {
		slow = slow.next;
		fast = fast.next.next;
		if (slow == fast) return true;
	}
	return false;
}
```
**Complexity**
Time complexity: O(n) because in two iterations, the slow and next pointers are bound to meet.
Space complexity: O(1)

### Entry point of the cycle.

**Problem statement**
Given a cyclic linked list, return the first(start) node of the cycle.

**Solution 1 (Get the length of the cycle)**
1. Let the slow and fast pointers meet (in the above code) at element `E`.
2. Take another pointer and move it 1 step further and count steps till it gets back to slow/fast pointer. This gives us the length of length of cycle. Say the length is `L`
3. Reset the slow and fast pointer  `slow = head, fast = head`
4. Move the fast pointer `L` times.
5. Then move the slow and fast pointer simultaneously. Wherever the two pointers meet, is the intersection

```java
Node intersection(Node head) {
	Node slow = head, fast = head;

	while (fast.next == null && fast.next.next == null) {
		fast = fast.next.next;
		slow = slow.next;
		if (slow == fast) break;
	}

	if (fast.next == null || fast.next.next == null) {
		throw new IllegalStateException("No cycle detected");
	}

	int lengthOfCycle = 1;
	fast = fast.next;
	while (slow != fast) {
		lengthOfCycle++;
		fast = fast.next;
	}

	slow = head, fast = head;
	for (int i=0; i<lengthOfCycle; i++) {
		fast= fast.next;
	}

	while (slow != fast) {
		slow = slow.next;
		fast = fast.next;
	}

	return slow;
}
```

**Solution 2**

- Supposed 
	- distance travelled before the cycle is `x`
	- Distance inside the cycle `l` (circumference of the circle)
	- Distance travelled by slow pointer other than `l` is `y`
- So, Distance travelled by slow pointer = `x + y + kl`
- Distance travelled by fast pointer = `x + y + ml`
- But fast pointer travels twice as much distance

```text
   x + y + kl = 2(x + y + ml)
=> x+y = (k-2m)l
```
- This implies that the the position where slow and fast pointer meet is a multiple of `l`
- So, similar to above approach, if we reset 1 pointer and move both slow and fast pointer 1 step at a time, they will meet at intersection.
- In other words, the point where the slow and fast pointer meet, is equal to distance from the head

```java
Node intersection(Node head) {
	if (head == null) return null;
	Node slow = head, fast = slow;

	while (fast.next != null && fast.next.next != null) {
		fast = fast.next.next;
		slow = slow.next;
	}

	if (fast.next != null && fast.next.next != null) return null;
	slow = head;
	while (slow != fast) {
		slow = slow.next;
		fast = fast.next;
	}
	return slow;
}
```

## Doubly Linked list

- Linked list with both `next` and `previous` pointers
- The first element is called `head`
- Last element is called `tail`
![[Pasted image 20240115212048.png]]
### Structure of a node

```java
class Node {
	int data;
	Node next;
	Node prev;

	Node(int x) {
		data = x;
		prev = null;
		next = null;
	}
}
```

### Insert a node

**Problem statement**
Given a doubly linked list, insert a node with data `x` at position `k` (K will always be a valid)

**Solution**
```java
Node insert(Node head, int x, int k) {
	Node n = new Node(x)
	if (head == null) {
		return n; 
	}
	if (k == 0) {
		n.next = head;
		head.prev = n;
		return n;
	}
	Node curr = head, pre = null;
	for (int i=0; i<k; i++) {
		pre = curr;
		curr = curr.next;
	}
	pre.next = n;
	n.prev = pre;
	n.next = curr;
	if (curr != null) {
		curr.prev = n;
	}
	return head;
}
```
**Complexity**
Time complexity: O(n) where n is the number of nodes in the given list
Space complexity: O(1)

### Delete a node from doubly linked list

**Problem statement** 
Given a doubly linked list of length N, delete the first occurrence of data 'x'.

**Solution**
```java
Node delete(Node head, int x) {
	if (head == null) return null;
	if (head.data = x) return head.next;

	Node curr = head;
	while (curr != null && curr.data != x) {
		curr = curr.next;
	}
	if (curr == null) return head;
	curr.prev.next = curr.next;
	if (curr.next != null) {
		curr.next.prev = curr.prev;
	}
	return head;
}
```

**Complexity**
Time complexity: O(n) where n is the number of nodes in the given list
Space complexity: O(1)