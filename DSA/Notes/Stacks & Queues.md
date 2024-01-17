
# Stack

Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

Use cases
- Recursion
- Undo-Redo functionality
## Operations on Stack

- `push(data)`:  Inserts data at the top of stack
- `pop()`: removes and returns the top element of the stack
- `peek()/top()`: Returns the top element of the stack
- `size()`: returns the size of the stack
- `isEmpty()`: Returns true if the stack is empty, false otherwise

> All these operations have time complexity of O(1)

## Implementation

- There are two ways to implement stack
	- Array based implementation
	- Linked list based implementation

### Array based implementation

- Start with an array of some `initial size`
- Initialise a variable `size = 0` . This variable refers to the top element is top element in the stack.
- To push data into the stack => `A[size++] = data`
- To pop, delete the last element from the array list and return it.

```java
class Stack {
	private static final int CAPACITY = 10;
	private List<Integer> arr = new ArrayList<>();

	void push(int data) {
		arr.add(data);
	}

	boolean isEmpty() {
		return arr.isEmpty();
	}

	int pop() {
		if (arr.isEmpty()) {
			return Integer.MIN_VALUE;
		}
		int x = arr.get(arr.size()-1);
		arr.remove(arr.size()-1);
		return x;
	}

	int peek() {
		if (arr.isEmpty()) {
			return Integer.MIN_VALUE;
		}
		return arr.get(arr.size()-1);
	}
}
```

**Limitations of array implementation**

1. Arrays are continuous allocation, so we may run out of memory => *Overflow condition*
2. If array elements are deleted, the memory never frees up.

### Linked list based implementation

- Singly linked list based implementation
- Insertion/deletion takes place at the `head`

```java
class Node {
	int data;
	int next;

	Node(int x) {
		this.val = x;
	}
}

class Stack {
	Node head;
	int size = 0;

	void push(data) {
		Node n = new Node();
		if (head == null) head = n;
		else {
			n.next = head;
			this.head = n;
		}  
		size++;
	}

	int size() {
		return size;
	}

	boolean isEmpty() {
		return size == 0;
	}

	int peek() {
		return isEmpty() ? return Integer.MIN_VALUE : head.val;
	}

	int pop() {
		if (isEmpty()) return Integer.MIN_VALUE;
		int data = this.head.data;
		size--;
		head = head.next;
		return data;
	}
}
```

## Questions

### Valid Parenthesis

**Problem statement**
Check whether a given sequence of parenthesis is valid.

**Solution**
```java
boolean isValidParenthesis(String s) {
	Stack<Character> stack = new Stack<>();

	List<Character> open = Arrays.asList('(', '{', '[');
	List<Character> close = Arrays.asList(')', '}', ']');
	
	for (char ch : s.toCharArray()) {
		if (open.contains(ch)) {
			stack.push(ch);
		} else {
			if (stack.isEmpty()) return false;
			char popped = stack.pop();
			if (ch != close.get(open.indexOf(popped))) {
				return false;
			}
		}
	}

	return stack.isEmpty();
}
```

**Complexity**
Time complexity: O(n) where n is the length of string
Space complexity: O(n) 

### Remove consecutive pair of equal characters

**Problem statement**
Given a string, remove the equal pair of consecutive characters.
Example:  
Input: abbc => Output: ac
Input: abbcbbcacx => Output: cx

**Solution**
```java
void removeConsecutive(String s) {
	Deque<Character> stack = new ArrayDeque<>();
	StringBuilder sb = new StringBuilder();

	for (char ch : s.toCharArray()) {
		if (!stack.isEmpty() && stack.peek() == ch) {
			stack.pop();
		} else {
			stack.push();
		}
	}
	String result = "";
    
    for (char ch : stack) {
        result += ch;
    }
	return result.reverse();
}
```

**Complexity**
Time complexity: O(n) where n is the length of string
Space complexity: O(n) 

