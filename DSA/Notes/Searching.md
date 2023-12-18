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