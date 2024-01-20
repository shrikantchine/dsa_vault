
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
Input: baa => Output: ba

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

### Post-fix expressions

- A mathematical operation looks like below (Also known as Infix operation)
	 `2 + 3`  (Here + is called operation and 2 & 3 are called operands)
- An infix expression is where operand is between the operator 
- The post-fix expression is where operand comes before the operator lie `2 3 +`

#### Infix to post fix conversion

| INFIX         | POST FIX      |
|---------------|---------------|
| 2 + 3         | 2 3 +         |
| 2 + 3 - 6 * 5 | 2 3 + 6 5 * - |
#### Evaluate a post fix expression
- Post fix operation can be evaluated using stack.
- Insert operands in stack
- When an operand is encountered, pop two elements and perform the operation and store the result back to the stack.


### Nearest Smaller element

**Problem Statement**
Given an integer array A, $\forall i$ find the index of nearest smaller element on the left of `i`

**Example**
```
A =                [8, 2, 4, 9, 7, 5, 3, 10]
Nearest elements = [-1, -1, 2, 4, 4, 4, 2, 3]
Indexes (Output) = [-1, -1, 1, 2, 2, 2, 1, 6]
```

**Brute force**
$\forall i$ loop back to from `i-1` to zero and find the first smaller element
Time complexity: O(n^2)

```java
int[] nearestSmaller(int[] arr) {
	int[] ans = new int[arr.length];
	ans[0] = -1;
	for (int i=1; i<arr.length; i++) {
		int j = i-1;
		int index = -1;
		while (j >= 0) {
			if (A[i] > A[j]) {
				index= j;
				break;
			}
			j--;
		}
		ans[i] = index;
	}
	return ans;
}
```

**Observation**
- Consider some array [8, x, x, x, x, 5, x, x, x, x]. For any element after 5, 8 can never be a solution
- So, we need to store all the potential answers for future elements
- Considering the two observations, use a stack as below
	- For each element `A[i]` pop out all values from stack that are greater than A[i]
	- Insert A[i]

**Optimised solution**

```java
int[] nearestSmaller(int[] A) {
	Deque<Integer> stack = new ArrayDeque<>();
	int[] ans = new int[A.length];

	for (int i=0; i<A.length; i++) {
		if (!stack.isEmpty()) {
			while (!stack.isEmpty() && A[stack.peek()] >= A[i]) {
				stack.pop();
			}
		}
		ans[i] = stack.isEmpty() ? -1 : stack.peek();
		stack.push(i);
	}

	return ans;
}
```

**Complexity**
Time complexity: O(n) because we can only remove and add an element at max once.
Space complexity: O(n) in case of already sorted ascending array

**Variations of this question**
1. $\forall i$ find the nearest smaller or equal element to the left of i.
2. $\forall i$ find the nearest greater element to the left of i.
3. $\forall i$ find the nearest greater or equal element to the left of i.
4. $\forall i$ find the nearest smaller element to the right of i.
5. $\forall i$ find the nearest smaller or equal element to the right of i.
6. $\forall i$ find the nearest greater element to the right of i.
7. $\forall i$ find the nearest greater or equal element to the right of i.

### Max area of rectangle from Histogram

**Problem statement**
Given an integer array A where A[i] is height of bar of histogram and width of each bar is 1.
Find the area of the largest rectangle formed by continuous bars

![[Pasted image 20240119225259.png]]

**Brute force**

$\forall subarray[i, j]$  calculate the are of find the max
Area = min(A[i...j]) * (j-i+1)

```java
int maxSubArea(int[] A) {
	int ans = 0;
	int minHeight = Integer.MIN_VALUE; // Carry forward approach
	for (int i=0; i<A.length; i++) {
		for (int j=i; j<A.length; j++) {
			int area = Math.min(minheight, A[j]) * (j-i+1);
			ans = Math.max(area, ans);
		}
	}
	return ans;
}
```

**Observations**
1. If we calculate the area for two indices, best time complexity is O(n^2) => Above code.
2. Better approach is to think about "for each height, what the best area that can be achieved"
3. For each height `A[i], 
	1. Find nearest smaller element to the left => `NSEL[i]`
	2. Find nearest smaller element to the right => `NSER[i]`
	3. Calculate the area using `Area = A[i] * ((NSER[i]-1) - (NSEL[i]+1) + 1)`
4. Edge case => if the `NSEL[i] or NSER[i] = -1`, in this case, include all elements


> [!NOTE] How to improve time complexity from quadratic to linear
> Change that thought process to think in terms of inputs which is linear

>[!TODO] Write code for this

**Complexity analysis**
Time complexity: O(n)
Space complexity: O(n)


> [!NOTE] How to do this in constant space
> Contents

### 

**Problem statement**
Given an integer array of size N, for all sub-arrays, find the (max-min) and return the sum of all.

**Example**

Given Array A= [2, 5, 3]

| Sub Array start index | Sub array end index | Min value in sub-array | Max value in sub array | Max-min |
|-----------------------|---------------------|------------------------|------------------------|---------|
| 0                     | 0                   | 2                      | 2                      | 0       |
| 0                     | 1                   | 5                      | 2                      | 3       |
| 0                     | 2                   | 5                      | 2                      | 3       |
| 1                     | 1                   | 5                      | 5                      | 0       |
| 1                     | 2                   | 5                      | 3                      | 2       |
| 2                     | 2                   | 3                      | 3                      | 0       |
Sum of Max-min = 8

**Brute force**
```java
int solve(int[] A) {
	int sum = 0;
	for (int i=0; i <A.length; i++) {
		int max = Integer.MIN_VALUE, min = Integer.MIN_VALUE;
		for (int j=i, j<A.length; j++) {
			max = Math.max(max, A[j]);
			min = Math.min(max, A[j]);
			sum += (max-min);
		}
	}
	return sum;
}
```

**Optimised approach**
- Like previous problem, going from quadratic to linear means for each element in the array, we perform some O(1) operation
- Here we can use the *Contribution Technique*
- We can observe here that
	- In all sub-arrays, where an element `x` is the maximum, it will contribute `+5`
	- In all sub-arrays, where an element `x` is the minimum, it will contribute `+5`
- So, contribution can be calculated as 
	- `Contribution = A[i] * ((No. of A[i] is max) - (No. of A[i] is min)`
- How to figure out "In how many sub-arrays A[i] is max" ?
	- Any element to the left that is greater than A[i] cannot be part of the subarray
	- Any element to the right that is greater than A[j] cannot be part of subarray
	- So Start index can be one of `A[NGEL+1 ... i]`
	- So Start index can be one of `A[i ... NGER-1]`
	- So total number of sub-arrays = `(i-NGEL) * (NGER-i)`
- Similarly for "In how many sub-arrays A[i] is min"
	- Total number of subarrays = `(i-NSEL) * (NSER-i)`

>[!Note] 
>NGER = Nearest greater element to right
>NGEL = Nearest greater element to left
>NSER = Nearest smaller element to the left
>NSEL = Nearest smaller element to the right

**Complexity**
Time complexity: O(n)
Space complexity: O(n)

## Queues: Implementation & Problems

- Queue is a linear data structure where the data is entered from the one end and retrieved from other in a First-In-First-Out (FIFO) order.

![[Pasted image 20240120211056.png]]

