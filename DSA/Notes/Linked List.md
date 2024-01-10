## Introduction

Linked List is a non-continuous linear data structure. Below are the advantages

1. Compared to arrays, it does not have a restriction of being continuous. So even in low continuous memory situations, linked list can be instantiated.
2. Compared to dynamic arrays, it only uses only the required space. In contrast dynamic arrays double their size which might result in unused space being allocated.

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
Given a linked list, return true if it is a palindrome.

**Solution**
```java
boolean isPalindrome(Node head) {
	
}
```