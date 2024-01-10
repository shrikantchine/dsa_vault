

## Prefix Sum

Prefix sum is the technique where you precompute & store the cumulative sum of the sequence of elements that allows fast sum calculation of any continuous range.

Let’s say we have a sequence of elements A as mentioned below-

```
A = {a0, a1, a2, a3, a4, a5}
so Prefix Sum P will be calculated as
P=  {p0, p1, p2, p3, p4, p5}

where-
p0 = a0
p1 = a1 + a0
p2 = a0 + a1 + a2
p3 = a0 + a1 + a2 + a3
p4 = a0 + a1 + a2 + a3 + a4
p5 = a0 + a1 + a2 + a3 + a4 + a5
```

### How it helps?

```
Q) Say we need to sum get sum of all elements from indices
 [2 to 5] => [a2 + a3 + a4 + a5]       or [p5 - p1]
 [1 to 4] => [a1 + a2 + a3 + a4]       or [p4 - p0]
 [0 to 4] => [a0 + a1 + a2 + a3 + a4]  or  [p4]

```

## Carry forward

The basic idea behind this technique is to keep track of previsouly calculate values and use it to calculate the next values.

For example, while calculating the maximum value from an array, naive approach is to compare each value with all other values. This can be optimized by keeping track of the maximum value seen so far and check that against the current value to see if any value exists that is can be greater than already seen value.

In this way, we are carrying forward the max value that we have seen so far.

## Sliding Window

- Window Sliding Technique is a computational technique that aims to reduce the use of nested loops and replace it with a single loop, thereby reducing the time complexity.
- Size of the window should be fixed
- The general use of the Sliding window technique can be demonstrated as follows:
    - Find the size of the window required
    - Compute the result for 1st window, i.e. from the start of the data structure
    - Then use a loop to slide the window by 1, and keep computing the result window by window.

## Questions

- ✔️Find equilibrium point of an array (Prefix sum and carry forward) [Code](./src/prefix_sum/EquilibriumPoint.java)
- ✔️Maximum sum subarray of size k [Code](./src/prefix_sum/MaxSumSubArr.java)


## Two pointers approach

- Two variables pointing to two elements in an array (this makes brute force approach same as Brute force approach in the question below)
- Two pointers approach requires answer to 2 questions ?
	- Where to initialise the 2 pointers ?
	- How to move the 2 pointers ?
- At each step, 1 element is rejected and search space is reduced.

### Pair with Given sum

**Problem statement**: Given a sorted integer array of size N and a number K, find any pair `(i, j)` such that `A[i] + A[j] = K` where `i != j`

**Approach 1 (Brute force)**
- Run linear search for each `K-A[i]`
- Time complexity: O(n^2)

**Approach 2 (Binary Search)**
- Run binary Search for each `K-A[i]`
- Time complexity: O(n log n )

**Approach 3 (Two pointers)**
- Initialise the pointer `i` to index `0`
- Initialise the pointer `j` to index 'n-1'
- Until `i` and `j` cross each other, 
	- Compute `A[i] + A[j]`
	- Check if the computed value against `K`
		- If it is equal, return `i & j`
		- If greater, `j--`
		- else `i++`

```java
int[] pairSumSortedArray(int[] arr, int k) {
	int i = 0, j = arr.length-1;

	while (i < j) {
		int sum = A[i] + A[j];
		if (sum == k) return new int[] {i, j};
		if (sum > k) j--;
		else i++;
	}

	return new int[] {-1, -1};
}
```

### Pair sum count

**Problem Statement**
Given a sorted integer array of size N and target element K, find the count of pairs such that `A[i] + A[j] = k AND i != k` 

**Solution**
The solution is same as above, except that we need answer the following question 

*When the first answer is found, how do we move the pointers i & j*

**Case 1:** If the elements in the array are distinct, then we move both `i` and `j` because no other element can be added in `A[i]` to make `k` 

```java
int pairSumCountSortedArray(int[] arr, int k) {
	int i = 0, j = arr.length-1, count = 0;

	while (i < j) {
		int sum = A[i] + A[j];
		if (sum == k) {
			count++;
			i++;
			j--;
		}
		if (sum > k) j--;
		else i++;
	}

	return count;
}
```


**Case 2:** If the elements in the array may be duplicate
- Count duplicates from either side, and add count, How ?
	- If `A[i] != A[j]` then `count += (frequency of A[i] * frequency of A[j])`
	- If `A[i] == A[j]` then `count += ` $nC2$  where n is the frequency of `A[i]`

//TODO Finish this
```java
int pairSumCountSortedArray(int[] A, int k) {
	int i = 0, j = A.length-1, count = 0;

	while (i < j) {
		int sum = A[i] + A[j];
		if (sum == k) {
		
		}
		if (sum > k) j--;
		else i++;
	}

	return count;
}
```


### 

**Problem statement**
Given a  sorted array of size N and value K > 0, find any pair `(i, j)` such that `i != j && A[j]-A[i] = K`

**Solution**
1. Since `k > 0, => A[j] > A[i] => j > i `. We can use two pointer approach.
2. Where to initialise the two pointers ?
	- i = 0 and j = n-1 will not work in case of negative numbers because difference will decrease if we increase i.
	- 

```java
int[] diffPair(int[] arr, int k) {
	int i=0, j=arr.length-1;

	while (i < j) {
		int diff = A[j] - A[i];
		if (diff == k) return new int[] {i, j};
		if (diff > k) {
			i++;
		} else {
			j--;
		}
	}

	return new int[] {-1, -1};
}
```