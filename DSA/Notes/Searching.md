```table-of-contents
```
### What is binary search ?
**Search Space**: The set of elements where the search is required to be performed.
**Target**: Element that is to be searched.

- Binary search is a method of searching an element where after constant amount of comparison, the search space is reduced to half.
- Binary Search is not only applicable for sorted data but for any data where the property 1 holds.
- *Searching in linear data-structure can only be done linearly or using binary search.*

> [!NOTE] Does binary search only apply to sorted data ?
> No. Check the question (Find unique element below)

### Structure of the binary search program
- Define a search space `[start, end]`
- Loop using the condition `(start <= end)`
- Find the mid element using `mid = start + ((end-start)/2)`
- Check if the middle element is the answer
- Check if we need to go left
- Check if we need to go right

### Find in sorted array

#### Problem statement
Given a sorted array of size N with distinct elements, search if a given element K is present or not (Return `true` of `false`)

#### Brute force solution
- Loop through all elements and find the element. 
- This is called `Linear Search`

```java
boolean linearSearch(int[] arr, int k) {
	for (int x : arr) {
		if (x == k) return true;
	}
	return false;
}
```

#### Binary Search
- For Linear search, we don't need sorted array.
- Since the array is sorted, the binary search can be used.

**Using recursion**

```java
void binarySearch(int[] arr, int k) {
	return binarySearch(arr, 0, arr.length-1, k);
}

boolean binarySearch(int[] arr, int start, int end, int k) {
	if (start > end) return false;
	int mid = start + ((end - start) / 2);
	if (arr[mid] == k) return true;
	if (arr[mid] < k) {
		return binarySearch(arr, mid+1, end, k);
	}
	return binarySearch(arr, start, mid-1, k);
}
```
**Complexity analysis**
Time complexity: O(log n)
Space complexity: O(log n)

**Without recursion**

```java
boolean binarySearch(int[] arr, int k) {
	int start = 0, end = arr.length-1;
	while (start <= end) {
		int mid = start + ((end - start)/2);
		if (arr[mid] == k) return true;
		else if (arr[mid] > k) {
			end = mid-1;
		} else {
			start = mid+1;
		}
	}
	return false;
}
```
**Complexity analysis**
Time complexity: O(log n)
Space complexity: O(1)

### Find first occurrence

**Problem statement** 
Given a sorted array of N elements and a target element, find the index of first occurrence of the target. If the target is not found, return -1;

**Solution**
- Find any occurrence of the target using binary search.
- Check the `mid-1` element to check if a better solution exists (Optional if we assume that it always exists)
- If yes. continue the binary search

**If we check the mid-1 element**
```java
int findFirst(int[] arr, int target) {
	int start = 0, end = arr.length-1;

	while (start <= end) {
		int mid = start + ((end - start) / 2);
		if (arr[mid] == target) {
			if (mid != 0 && arr[mid] == arr[mid-1]) {
				end = mid-1;
			}
			return mid;
		}
		else if (arr[mid] < target) {
			start = mid + 1;
		} else {
			end = mid-1;
		}
	}

	return -1;
}
```

**If we assume that there is a better solution already**
```java
int findFirst(int[] arr, int target) {
	int start = 0, end = arr.length-1, ans = -1;
	while (start <= end) {
		int mid = start + ((start-end) / 2);
		if (arr[mid] == target) {
			ans = mid;
			end = mid-1;
		} else if (arr[mid] < target) {
			start = mid+1;
		} else {
			end = mid-1;
		}
	}
	return ans;
}
```

**Complexity analysis**
Time complexity: O(log n)
Space complexity: O(1)


> [!NOTE] How to find the last occurrence
> Same approach can be used. Instead of checking the left size after find an occurrence, check the right side.


> [!NOTE] How to find the count of given elements
> Find the first element and last element using the above approaches and use the below formula 'end - start +1' to find the count.

### Find unique element

**Problem statement**
Given an integer array of size N where every element except one occur twice. One element occurs only once. Find the unique element if the duplicate elements are placed next to each other.

**Example**
Given A = [8,8,5,5,6,2,2] => Ans = 6

**XOR all elements**
- Take XOR of all elements and return and return the value
- Time complexity = O(n)
- This approach does not make use of the fact that duplicate elements are placed next to each other.

**Binary search approach**
1. Find the mid element
2. Check if it is the unique element 
	1. Compare it with left and right element 
	2. If yes, return the element
3. Step to the first occurrence of the element at mid
4. Calculate the length of the elements till `mid-1`. If they are odd, the unique element is present in left. Otherwise the element is present on right.
5. So, based on step 4, reduce the search space and continue.

```java
int findUnique(int[] arr) {
	int start = 0, n = arr.length,  end = n-1;

	while (start <= end) {
		int mid = start + ((end - start)/2);
		if ((mid == 0 || arr[mid] != arr[mid-1]) && (mid==(n-1) || arr[mid] != arr[mid+1])) {
			return mid;
		}
		if (mid != 0 && arr[mid-1] == arr[mid]) {
			mid -= 1;
		}
		if ((mid-start) %2 == 0) {
			start = mid + 2;
		} else {
			end = mid - 1;
		}
	}
}
```

**Complexity analysis**
Time complexity: O(log n)
Space complexity: O(1)

### Find max from increasing-decreasing array

- Given an increasing-decreasing array, find the max element.
- An increasing-decreasing array is where the elements first increase and then decrease.

Example:
[1, 3, 5, 10, 15, 12, 8, 6]


### Find local minima

**Problem statement** 
Given an array of N distinct elements, find any local minima
Local minima is defined by below condition
$A[i] < A[i-1] and A[i] > A[i+1]$

**Brute force**
For all elements, check if the previous and following element is greater than it while checking for boundaries.

```java
int findMinima(int[] arr) {
	for (int i=0; i<arr.length; i++) {
		if ((i == 0 || arr[i]<arr[i-1]) && (i == (arr.length-1) || arr[i] < arr[i+1])) {
			return arr[i];
		}
	}
}
```
**Complexity analysis**
Time complexity => O(n)
Space complexity => O(1)

**Binary Search**

- Find the mid element.
- If it is local minima, return it.
- If not, check if mid-1 is smaller than mid element, if so, move the search space to [start, mid-1]
- If mid+1 is smaller, the move the search space to [mid+1, end]

*The reason this works, if we can find a smaller element on either side, that side is bound to have a local minima*

```java
int findLocalMinima(int[] arr) {
	int start = 0, N = arr.length, end = N-1;

	while (start <= end) {
		int mid = start + ((end-start)/2);
		if ((mid == 0 || arr[mid] < arr[mid-1]) && (mid == (n-1) || arr[mid] < arr[mid+1])) {
			return arr[mid];
		}
		else if (mid == 0 || arr[mid-1] < arr[mid]) {
			end = mid-1;
		} else {
			start = mid+1;
		}
	}
	return -1;
}
```
**Complexity analysis**
Time complexity => O(log n)
Space complexity => O(1)

> [!NOTE] Local minima when duplicate elements are allowed
> Think of a solution

### Search in sorted rotated array

**Problem statement**
Given an array of N integer sorted and rotated. Find the given element K.

**Observations**
- Any sorted rotated array can be divided into two arrays (`A1` and `A2`) which are sorted. `concat(A1, A2) = givenarray`
- All elements in `A2` will be smaller than all elements in `A1`
- Below cases can be considered
	- The mid element is part of `A1`=> `A[mid] > A[end]`
		- All elements `[start, mid]` will be increasing
		- So, go to left if `A[start] <= k < A[mid]` else go right
	- *ELSE* The mid element is part of `A2` => `A[mid] < A[end]`
		- All elements in range `[mid, end]` will be increasing
		- So, go to right if `A[mid] < k <= A[end]` else go left
	- Concatenating `A1` ad `A2` may for a sorted array. Can be checked using `A[0] < A[N-1]`
- 

**Binary Search approach 1**
- Find where the array is rotated 
- Then run Binary search against the part of array that contains the element

> [!NOTE] HOME WORK
> Write code

**Binary Search Approach 2**

```java
int searchInRotated(int[] arr, int k) {
	int start = 0, end = arr.length-1;

	while (start <= end) {
		int mid = start + ((end-start)/2);
		if (arr[mid] == k) return k;
		if (arr[start] <= arr[mid]) {
			if (arr[start] <= k && arr[mid] > k) {
				end = mid-1;
			} else {
				start = mid+1;
			}
		} else {
			if (arr[mid] < k && arr[end] >= k) {
				start = mid +1;
			} else {
				end = mid-1;
			}
		}
	}
	return -1;
} 
```
**Complexity analysis**
Time complexity => O(log n)
Space complexity => O(1)

### Find Square root

**Problem statement**
Given an integer N, find the value of square root of N.

> This problem statement belongs to category of *Binary Search on Answer space*

Example:

| N                            | Answer |
|------------------------------|--------|
| 36                           | 6      |
| 49                           | 7      |
| 52                           | 7      |
| Any number in range [50, 63] | 7      |
| 64                           | 8      |

**Brute Force**
For the range `[1, N]`, calculate `i*i`

```java
int sqroot(int N) {
	for (int i=1; i<N; i++) {
		int sq = i*i;
		if (sq == N) return i;
		if (sq < N) return i-1;
	}
	return -1;
}
```
**Complexity analysis**
Time complexity => O($\sqrt N$) $\because$ At most the loop runs till $\sqrt N + 1$ 
Space complexity => O(1)

**Observation**
- For a given number N, $\sqrt N$ is in the range `[1, N]`
- In the brute force, as the value of `i` increases, so does the values of $\sqrt N$


> [!NOTE] When Binary search on answer space can be used?
> 1. Answer space is continuous
> 2. Answer space is sorted

**Solution**
- Define the answer space as `[start, end] = [1, N]`
- Find the mid element. 
- Square the mid element
- Check if it is equal to N, if yes, return it.
- If the square is greater than N, reject the right answer space by reducing the answer space `[start, mid-1]`
- Else reject the left answer space by changing the answer space to `[mid+1, end]`

```java
int sqroot(int N) {
	int start = 1, end = N;

	while (start <= end) {
		int mid = start + ((end-start)/2);
		int square = mid * mid;
		// No need for this because it is handled in <= condition
		// if (square == N) return mid;
		if (square <= N) {
			int tmp = (mid+1) * (mid+1);
			if (tmp > N) {
				start = mid+1;
			} else {
				return mid;
			}
		} else {
			end = mid-1;
		}
	}

	return -1;
}
```

**Complexity analysis**

Time complexity => O(log N)
Space complexity => O(1)

### Ath Magical Number

**Problem statement** 
Given three integer A, B and C, find the Ath magical number. A magical number is a number which is divisible by B or C or both.

**Example**
Given A = 8,, B = 2, C=3 
=> Answer = 12 (Number are 2, 3, 4, 6, 8, 9, 10, 12)

**Brute force**
- Initialise current value as 1 and counter as 0
- Check if it is divisible by B or C, if yes, increment the counter.
- Increment the current value by and check divisibility with B or C.
- If counter == A, return the number

```java
int athMagical(int A, int B, int C) {
	int counter = 0, current = 1;
	while (counter < A) {
		if (current % B == 0 || current % C == 0) {
			counter++;
		}
		current++;
	}
	return current;
}
```

**Complexity Analysis**
- Consider the inputs from the examples taken
- 8<sup>th</sup> no divisible by 2 is `8*2`
- 8<sup>th</sup> no divisible by 3 is `8*3`
- There can be overlap if we consider 8th number divisible by 2 and 3. But to upper bound this(Overlap will not exist if C=20), we will find the 8th magic number in `8*2` iterations

*Therefore, time complexity: O(A * min(B, C))*

**Optimised Approach using Binary Search**

- We can define the answer space as `[1, min(B, C)*A]`
	- It is continuous
	- It is sorted
	- The pattern is increasing. Meaning going to left decreases the number of magic numbers and vice versa
- If we can find the number of magic numbers present to the left of a given number in the range, then we can decide to go either left and right and reduce the answer space to half as per binary search algorithm.
- How to check the number of magical numbers less than or equal to a given number X
	$\frac X B +\frac X C - \frac X {B \space and \space C}$
	
	$OR\space\space \frac X B +\frac X C - \frac X {LCM(B,C)}$
	
- How to check the mid element 
	- Find the count using above approach
	- Check if mid element itself is a magical number, if yes, return
	- Otherwise, move to left because we will always find the Ath middle element on the left side.

```java
int athMagicalNumber(int A, int B, int C) {
	int start = 1, end = Math.min(B, C)*A;
	int lcmBC = lcm(B, C);
	while (start <= end) {
		int mid = start + ((end-start)/2);
		int count = (mid/B) + (mid/C) - (mid/lcmBC);

		if (count == A) {
			if (mid % B == 0 || mid % C == 0) return mid;
			end = mid - 1;
		} else if (count < A) {
			end = mid - 1;
		} else {
			start = mid + 1;
		}
	}
}
```

**Complexity**
Time complexity: O(A * Min(B, C))
Space complexity: O(1)

### Painter's partition

**Problem statement**
Given N boards with their lengths as array A = [L0, L1, L2....L(N-1)]
And given K painters, each painter takes 1 unit of time to paint 1 unit of length.
Calculate the min amount of time in which all boards can be painted.

==Note==
1. Two painters cannot share a board to paint.
2. A painter will only paint a continuous board

**Example**

1. A=[4],  k = 1, Ans  = 4 (1 painter takes 4 units to paint a board of length 4)
2. A = [3, 5, 1, 7, 8, 2, 5, 3, 10, 1, 4, 7, 5, 4, 6], K = 3
3. A = [10, 20, 30, 40], k=2 => Ans = 60

**Observations**
- If we have infinite number of painters, the min time taken will be `max(board lengths)`
- If we have 1 painter, the min time taken will be `sum(length of boards)`
- So, the range of ans `[max length, sum of all lengths]`. This forms the answer space
- how to figure out whether to go left or right => Given an element X, is it possible to paint all boards in X units of time with K painters ?
	- For each painter, allocate the max amount of time <= X from the boards array

```java
boolean check(int[] A, int T, int K) {
	int painters = 1, i = 0;

	while (painters <= K) {
		int unitsConsumed = 0;
		while (unitsConsumed <= T) {
			unitsConsumed += A[i++];
			if (i == A.length) return true;
		}
		painter++;
	}

	return false;
}

// OR 

boolean check(int[] A, int T, int K) {
	int curr_time = T;
	int count = 1;
	for (int i=0; i<A.length; i++) {
		if (A[i] <= curr_time) {
			curr_time;
		} else {
			count++;
			curr_time = T;
		}
		if (count > K) return false;
	}
	return true;
}
```

- Now we can do binary search using the above answer space and condition to check

```java
int minTime(int[] A, int k) {
	int s = max(A);
	int e = sum(A);

	while (s <= e) {
		int mid = s + ((e-s)/2);
		if (check(A, mid, K)) {
			if (check(A, mid-1, K)) {
				e = mid -1;
			}
			return mid;
		} else {
			s = mid+1;
		}
	}
}
```

**Complexity analysis**

Time complexity = N * log (sum(A) - max(A))