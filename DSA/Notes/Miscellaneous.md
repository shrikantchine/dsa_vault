
### Perfect numbers

**Problem statement**
Given an integer A, find the Ath perfect number. 

Perfect number:
- Comprises of 1 and 2
- The number of digits are even
- It is a palindrome

**Example**

| Number | is Perfect number ? |
| ------ | ------------------- |
| 11     | yes                 |
| 111    | no                  |
| 12     | no                  |
| 22     | yes                 |
| 123    | no                  |
| 1111   | yes                 |
| 112211 | yes                 |
| 2212   | no                  |
**Solution**

- Perfect number series
```
11, 22, 1111, 1221, 2112 ...
```

- Since all these numbers are palindrome, lets look at the first half and build the series
```
1, 2, 11, 12, 21, 22 ...
```

- So, the approach could be
	- Use a queue data structure
	- Insert 1 and 2 in the queue.
	- Remove the front of the queue.
	- Append 1 to it for the next number, insert it into the queue.
	- Append 2 to it for the next number, insert it into the queue.

```java
String perfectNumber(int A) {
	if (A == 1) return "11";
	if (A == 2) return "22";
	
	Deque<String> queue = new LinkedList<>();
	queue.addLast("1");
	queue.addLast("2");
	StringBuilder answer = new StringBuilder();
	int count = 3;

	if (count <= A) {
		StringBuilder sb = new StringBuilder(queue.poll());
		if (count == A) {
			answer = sb;
			break;
		}
		sb.append("1");
		queue.add(sb.toString());
		sb.deleteCharAt(sb.length()-1);
		sb.append("2");
		queue.add(sb.tostring());
		count++;
	}

	return ans.toString() + sb.reverse().toString();
}
```

### Flip Array

**Problem Statement**

Given an array **A** of positive elements, you have to flip the sign of some of its elements such that the resultant **sum** of the elements of array should be minimum non-negative(as close to zero as possible).

Return the minimum number of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.

**Example**:
```
A = [10, 15, 6, 3, 3]
Answer : 2
Result array: [10, -15, 6, -3, 3]
```

**Brute force Solution**

- Choice: Flip or not flip
- Use backtracking to generate all possible cases.
- Calculate sum of all base cases from backtracking tree.
- If sum < 0 => Ignore
- If sum > currentMinNegative => Ignore
- if sum == min non negative sum => compare number of flips
- if sum < min non negative sum => update min non negative sum
- return flips.

**Optimisation 1**

- Calculate the contribution of flipped elements
	- For each flipped element, add the value to x leaving the remaining value in y.

```
If S = Total Sum, x = Sum of flipped elements, y = remaining sum
x + y = S
=> y>= x (based on problem statement)
=> S-x >= x
=> x <= S/2
```

- This implies that total sum of flipped elements cannot go beyond `S/2`
- This fact can be used to prune backtracking tree branches.

**Optimisation 2**

- Since the sub-problems do not return an answer, it cannot be optimised using memoization.
- Considering the optimisation from above, since the max sum of flipped elements is $\lfloor s/2 \rfloor$
- So, we build recursive state using the index  and remaining sum
- This is same as 0-1 knapsack
	- Remaining sum = Capacity of knapsack
	- Since selecting an element means flipping an element => 1 flip contributes 1 to the value.
	- Weights is the array given.
	- Instead of maximising the value, in this case we need to minimise the value

```java
int flipArray(int[] A, int index, int remaningSum) {
	if (remainingSum == 0) return 0;
	if (index == -1) return 0;
}
```

### Ways to form max heap

**Problem statement**

Given an integer N, find ways to form max heap with N distinct numbers.

**Observations**
- Counting the ways to form a heap does not depend on the values of the N numbers
- If the number of nodes are fixed, the structure of the tree is fixed
	- Height will be fixed
	- Complete binary tree.
	- max node is always the maximum value
- Possible value for any root node = 1
- There is no relationship between left and the right sub-tree.
- Thus to figure out the all the ways to create a heap
	- Fix the root node
	- Divide the rest (N-1) elements into left and right subtree.
- When you select number of elements for the left, right side is automatically selected. 
- How to select nodes for left sub tree = `n C l` where l is the number of nodes selected for left sub-tree.
- Thus our recurrence relationship is

$$
ways(N) = \binom {N-1}{L} * ways(L) * ways(R)
$$
- How to find the value for L ?
	- Both left and right sub tree have equal nodes 
	- Number of nodes at a given level `k = 2^k`
	- Consider height is defined by $H = \lfloor log N \rfloor$
	- Max nodes at the last level = 2^H
	- Total number of nodes till H-1 level = $2^0 + 2^1 + ... 2^H-1 = 2^H-1$ (Using GP)
	- Total number of nodes in the last level == $N-(2^H-1)$ 
	- Total number of nodes in left sub tree
$$
	= min(2^(H-1), N-(2^H-1))
$$

- Therefore the value of L =
$$
	\begin{align*}
	x = 2^(H - 1) \\
	l = (x-1) + min(x, (N-(2x-1))
	\end{align*}
$$

```java
int noOfways(int N) {
	if (N <= 0) return 1;
	int height = (int) Math.log(N);
	int x = Math.pow(2, height-1);
	int l = (x-1) + Math.min(x, N-(2x-1));
	int r = N-l-1;
	int ways = combination(N, l) * noOfways(l) * noOfways(r);
	return ways;
}
```

> add memoization since we have repeating sub problems

### Intersecting cords

**Problem statement**
Given a number **A**, return number of ways you can draw **A** chords in a circle with **2 x A** points such that no **2** chords intersect.

Two ways are different if there exists a chord which is present in one way and not in other.

### Max rectangle in binary matrix

**Problem statement**

Given a 2-D binary matrix A of size `N x M` filled with **0's** and **1's**, find the **largest** rectangle containing **only ones** and return its **area**.

**Brute force**
- for every sub-matrix, check if it only contains 1.
	- Can be done with 4 level nested loop to define 2 diagonally opposite corners of the matrix.
- If so, sum it up to get the area
	- This can be done with 2 level nested loop
- Compare it to global maximum and if it is larger, update global max
- Total time complexity: O(n^3 m^3)
- Space complexity: O(1)

