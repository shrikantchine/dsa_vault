```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
## Counting sort

### Return smallest number defined by an array

**Problem statement:** 

Given an array of N elements representing the digits of an array, return an array that represents the smallest number formed by the digits.

**Approach 1**

Sort the array and return it.
Time complexity: O(n log n)

**Observations**

1. 0 ≤ A[i] ≤ 9
2. Observation 1 can be used as frequency array.

**Efficient approach**
1. Create an array of size 10.
2. Loop through the elements of an array and save the frequency of each element.
3. Loop through frequency array and update the input array using the frequency of elements (as shown below).

```java
void rearrangeDigits(int[] nums) {
	int[] freq = new int[10];
	int index = 0;
	for (int i=0; i<nums.length; i++) {
		freq[nums[i]]++;
	}
	for (int i=0; i<10; i++) {
		int val = freq[i];
		while (val > 0) {
			nums[index] = i;
			index++;
			val--;
		}
	}
}
```

### When to use Counting sort ?
- Counting sort cannot be used when
	- Element size is unknown.
	- Element size is huge.
- Counting sort should be preferred when the size is around `~10^6`
- If there are negative numbers, offset the numbers by subtracting `min(A[i])`
	- Find the range i.e. min and max element in the array.
	- Size of the frequency array `maxElement - minElement + 1`. This is derived using 
		$No \space of \space elements \space in \space range \space [s, e]= e-s+1$
	- frequency of any element `x` will be stored on index `X - minElement`.

```java
void rearrange(int[] nums) {
	int min = Integer.MAX_VALUE, max = Integer.MAX_VALUES;
	for (int x : nums) {
		min = Math.min(min, x);
		max = Math.max(max, x);
	}
	int[] freq = new int[max - min + 1];
	for (int i=0; i<nums.length; i++) {
		freq[i-min]++;
	}
	int idx = 0;
	for (int i=0; i<freq.length; i++) {
		int val = freq[i];
		while (val > 0) {
			nums[idx] = freq[i] + min;
			idx++;
			val--;
		}
	}
}
```


## Merge Sort
### Sort when even and odd are relatively sorted

**Problem statement**
Given an integer array where the odd valued elements are relatively sorted & even values are relatively sorted. Sort the complete array.

**Example**
A = [2, 5, 4, 8, 11, 13, 10, 15, 21]
- All odd elements [2,4, 8, 10] are already sorted
- Similarly odd elements [5, 11, 13, 15, 21] are already sorted.

**Approach 1 (Basic sorting)**
1. Sort the elements
2. Time complexity: O(n log n)

**Observations**
1. If we split the array into two arrays such that
	1. Even array of size `E` contains all even elements 
	2. Odd array of size `O` contains all odd numbers
2. Use two pointers `i and j` pointing to the first elements of each array
3. Use the below formula to calculate the element
	```
	SortedArr[idx] = min(E[i], O[j])
	```
4. Increment the index that had the min element.

```java
void splitAndMerge(int[] nums) {
	int sizeOdd = 0, sizeEven = 0;
	for (int x : nums) {
		if (x%2 == 0) sizeEven++;
		else sizeOdd++;
	}
	int[] evens = new int[sizeEven];
	int[] odds = new int[sizeOdd];
	int i=0, j=0, idx=0;

	// Split
	for (int x : nums) {
		if (x%2 == 0) evens.add(x);
		else odds.add(x);
	}

	// Merge
	while (i < evens.length && j <= odds.length) {
		if (evens[i] > odds[j]) {
			nums[idx++] = j++; 
		} else {
			nums[idx++] = i++;
		}
	}
	while (i < even.length) {
		nums[idx++] = i++;
	}
	while (j < odd.length) {
		nums[idx++] = j++;
	}
}
```

### Merge sort algorithm
1. Split the given array into two equal or approximately equal arrays
2. Keep sorting using recursion until the base case is reached (If length of array is 1, array is already sorted)
3. Use the merge step from previous question to merge the sorted arrays.

```java
void mergeSort(int[] nums) {
	int n = nums.length;
	mergeSort(nums, 0, n-1);
}

void mergeSort(int[] nums, int start, int end) {
	if (start >= e) return;
	int mid = start + ((end-start) / 2);
	mergeSort(nums, start, mid);
	mergeSort(nums, mid+1, end);
	merge(nums, start, mid, end);
}

void merge(int[] nums, int start, int mid, int end) {
	int[] left = new int[mid-start+1];
	int[] right = new int[end-mid];
	int leftIdx = 0, rightIndx = 0, idx = start;

	for (int i=start; i<=mid; i++) {
		left[i-start] = nums[i];
	}
	for (int i=mid+1; i<end; i++) {
		right[i-mid-1] = nums[i];
	}
	while (leftIdx < left.length && rightIdx < right.length) {
		if (left[leftIdx] < right[rightIdx]) {
			nums[idx++] = left[leftIdx++];
		} else {
			nums[idx++] = right[rightIdx++];
		}
	}
	while (leftIdx < left.length) {
		nums[idx++] = leftIdx++;
	}
	while (rightIdx < right.length) {
		nums[idx++] = rightIdx++;
	}
}
```
### Complexity analysis for merge sort

#### Time complexity
1. Dividing the array requires `O(log N)`
2. Merging the array requires `O(log N)`
3. Each merge step requires `O(N)` (Consider the upper bound)

Adding these up:
Time complexity = `O(log N + N log N)` = `O(N log N)`

#### Space complexity
1. Number of concurrent recursion is `O(log N)`
2. Each merge step uses `O(N)`

Adding them up:
Space complexity: O(N)

#### Recurrence relationship

$T(N) = 2T (\frac N 2) + N$

### Inversion pair count in an array

**Problem statement**

Given an array of integers **A**. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A.

**Brute force**
For all elements at index i, look for all elements to the right (call it index j) and check how many satisfy the condition A[i] > A[j]. 

```java
void inversionPair(int[] nums) {
	int count = 0;
	for (int i=0; i<nums.length; i++) {
		for (int j=i+1; j<nums.length; j++) {
			if (A[i] > A[j]) count++;
		}
	}
	return count;
}
// Time complexity: O(n^2)
// Space complexity: O(1)
```

**Optimised approach**
- Observation 1: For each element, we need to find the number of elements that are after the element in given array but should be before in sorted array.
- How to use merge step of merge sort to solve this ?
	- In the merge step, we have 2 sorted arrays `left` and `right`
	- If any merge step, we select an element from `left` array, contribution towards inversion count is zero.
	- If we select an element from `right` array, the contribution towards the inversion count is the number of elements not yet added to answer from the left array.

```java
int inversionCount(int[] nums) {
	return mergeSort(nums, 0, nums.length);
}

int mergeSort(int[] nums, int start, int end) {
	if (start >= end) return 0;
	int mid = start + ((end - start) / 2);
	int count = mergeSort(nums, start, mid);
	count += mergeSort(nums, mid+1, end);
	return count + merge(nums, start, mid, end);
}

int merge(int[] nums, int start, int mid, int end) {
	int[] left = new int[mid-start+1];
	int[] right = new int[end-mid];
	int count = 0, leftIdx = 0, rightIndx = 0, idx = start;;

	for (int i=start; i<=mid; i++) {
		left[i-start] = nums[i];
	}
	for (int i=mid+1; i<end; i++) {
		right[i-mid-1] = nums[i];
	}

	while (leftIdx < left.length && rightIdx < right.length) {
		if (left[leftIdx] < right[rightIdx]) {
			nums[idx++] = left[leftIdx++];
		} else {
			nums[idx++] = right[rightIdx++];
			count += (left.length - leftIdx);
		}
	}
	while (leftIdx < left.length) {
		nums[idx++] = leftIdx++;
	}
	while (rightIdx < right.length) {
		nums[idx++] = rightIdx++;
	}
} 
```

## Pivot partitioning and Quick sort

### Segregate zeros and one's

**Problem statement**
Given an array of N elements containing 0's and 1's. Segregate all zeros on left and 1's on right 

**Count sort**
1. Count the number of zeros. Say the count is X.
2. Set first X elements to 0 and rest of the elements to 1.

**More**
1. Set variable `i` to the first `1`
2. Set `j = i+1`
3. Every time we encounter `0` at index `j`, we swap `i` and `j`. 
	1. This way the condition that that i points to first `1` holds
	2. j is used to iterate.

```java
void segregateZeros(int[] nums) {
	int i = 0;
	while (nums[i] != 1 && i < nums.length) {
		i++;
	}

	for (int j=i+1; j<nums.length; j++) {
		if (A[j] == 0) {
			int tmp = A[i];
			A[i] = A[j];
			A[j] = tmp;
			i++;
		}
	}
}
```

### Pivot partitioning

**Problem statement**
Given an integer array &&  a pivot element, we need to arrange the array such that all elements left of pivot are smaller than pivot while all elements to the right, are greater.

**Example**
Given: A = [54, 26, 93, 17, 77, 31, 44, 55, 20] AND pivot element is 54
Ans: A = [31, 26, 20, 17, 44, 54, 77, 55, 93]

**Observation**
- We can do this using the approach in previous question.

**Approach**
1. Initialise `i` to the first element greater than pivot
2. Initialise `j = i+1`
3. Iterate j till the length of array and when an element less than pivot element is found.
	1. Swap it with `ith` element
	2. increment `i`

```java
void partition(int[] arr, int pivot) {
	int i=0;

	while (i < arr.length && arr[i] < pivot) {
		i++;
	}

	for (int j=i+1; j<arr.length; j++) {
		if (arr[j] < pivot) {
			swap(arr, i, j);
		}
	}

	for (int j=i+1; j<arr.length; j++) {
		if (arr[j] == pivot) {
			swap(arr, i, j);
			break;
		}
	}
}

private void swap(int[] arr, int j, int i) {
	int tmp = arr[j];
	arr[j] = arr[i];
	arr[i] = tmp;
}
```

### Quick sort
- This is a divide an conquer algorithm
- The goal is to select a pivot and run partition algorithm
- Why does this work ?
	- After partition algorithm, pivot element is correctly placed 
	- After partition algorithm, all elements greater that pivot are on right side. Same for smaller elements.

**Algorithm steps**
1. Select a pivot element
2. Partition the array into left and right based on pivot element
3. Recursively call quick sort on left and right.

```java
void quicksort(int[] A) {
	quicksort(A, 0, A.length-1);
}

void quicksort(int[] nums, int start, int end) {
	if (start >= end) return;
	// Partition in range [start, end] and pivot element is decided by partition function
	int pi = partition(nums, start, end); 
	quicksort(nums, start, pi-1);
	quicksort(nums, pi+1, end);
}
```

## Comparable

### Sort based on factors

**Problem statement**
Given an array of N integers, Sort the data in ascending order of count of factors. If two numbers have same number of factors, return them in ascending order of their values.

**Example**
```
A                = [9, 3, 10, 6, 4]
count of factors = [3, 2,  4, 4, 3]
Output           = [3, 4, 9, 10, 6]
```

**Using Comparator**
1. Define a compare function as below
```java
// Should return -ve if count of factors of A < count of factors of B
// Should return +ve if count of factors of B < count of factors of A
// Should return 0 otherwise
int compare(int A, int B) {
	int factorsA = getFactors(A);
	int factorsB = getFactors(B);

	if (factorsA < factorsB) {
		return -1;
	} else if (factorsA > factorsB) {
		return 1;
	} else {
		return Integer.compare(A, B);
	}
}

private int getFactors(int a) {
	int count = 0;  
	for (int i=1; i*i <= a; i++) {  
		if (a % i == 0) {  
			if (i * i == a) count += 1;  
			else count += 2;  
		}  
	}  
	return count;
}
```
2. Use the `sort` function as below
```java

void sortByFactors(int[] A) {
	Arrays.sort(A, new Comparator<Integer>(){
		@Override
		public int compare(Integer a, Integer b) {
			return compare(a, b); // Use the above defined method.
		}
	});
}
```
