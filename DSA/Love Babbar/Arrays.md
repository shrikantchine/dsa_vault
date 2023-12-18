---
tags:
  - 1-Darray
  - 2d-array
aliases:
  - 1-D Array
---

```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
Ref: [[1-D array]] && [[2-D Array]]

### 1. Reverse the array

**Problem statement**
Given an array of size N and an integer value M, reverse the elements of the array starting at position M.

**Solution**
```java
void reverseArray(ArrayList<Integer> arr, int m) {
	int n = arr.size();
	int i=m+1, j=n-1;
	while (i < j) {
		Collections.swap(arr, i++, j--);
	}
}
```

**Complexity analysis**
Time complexity: O(n)
Space complexity: O(1)

### 2. Sum of min and max

**Problem statement**
Given an array of size N, find the sum of its max and min values

**Solution**
```java
int sumMinMax(int[] arr) {
	int min = Integer.MAX_VALUE, max = Integer.MAX_VALUE;
	for (int x : arr) {
		min = Math.min(min, x);
		max = Math.max(max, x);
	}
	return min + max;
}
```

**Complexity analysis**
Time complexity: O(n)
Space complexity: O(1)

### Kth Smallest element in an array

**Problem statement**: Given an array of size N and an integer K s.t. K < N. Find the K<sup>th</sup> smallest element from the array.

**Approach 1: Sorting**
- Sort the array 
- Return k-1<sup>th</sup> element
- 

```java
void kthSmallest(int[] arr, int k) {
	Arrays.sort(arr);
	return arr[k-1];
}
```

**Approach 2: Quick Select algorithm**

[Quick select algorithm on GFG](https://www.geeksforgeeks.org/quickselect-algorithm/)
[[Sorting]] -- Quick sort
- Quick select algorithm makes use of the `partition` function described in Quick Sort algorithm.
- The difference is that instead of sorting both sides of pivot recursively, it aims to find the  pivot element at index `k-1`
- Following approach is used
	- Initialise `left = 0` and `right=n-1`
	- Select a pivot element between left and right.
	- Run the partition algorithm with the selected pivot. Partition algorithm returns the index of the pivot `pivotIndex`
	- if `k == pivotIndex` return the pivot element
	- if `k < pivotIndex`: Recursively call the left side
	- Else recursively call the right side.

```java
int partition(int[] arr, int left, int right) {
	int pivot = arr[right];
	
	for (int i=left; i<=right; i++) {
		if (arr[i] < pivot) {
			
		}
	}
}

int kThSmallest(int[] arr, int k) {

}
```
