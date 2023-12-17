```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
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

### 