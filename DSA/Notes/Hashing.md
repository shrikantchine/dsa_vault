# Hashing

# ⭐️What is Hasing ?

- Given is when a function `f()` maps infinite amount of values a set of finite values
- An example of Hash Function is the module operator `%`

# ⭐️Hash Table vs Hash Map vs Hash Set

- Hash Table is like a pattern (A theoretical concept)
- Hash Map is the implementation
- Searching for a key is O(1)
- Keys in a HashMap are unique but values may not be unique.
- Hash Set stores unique keys and provides O(1) retrieval

## Methods of HashMap (Pseudo code)

```java
- insert(key, value) // Adds new key value to the hashmap
- update(key, value) // updates existing key's value
```

# ⭐️Questions

1. Given an interger array of size N, find the frequency of each element in Q queries.

```java
/**
Brute force version:
    For every query => Iterate and count the frequency of an array
    Time complexity: O(Q*N)
    Space complexity: O(1)

How to improve ?
    Pre-compute the count of frequencies for each element and store in HashMap.
    Time Complexity: O(Q + N)
    Space complexity: O(N)
*/

void countFrequencies(int Q[], int A[]) {
    HashMap<Integer, Integer> frequencyMap = new HashMap<>();
    for (int i=0; i < A.length; i++) {
        if (!frequencyMap.containsKey(A[i]) frequencyMap.insert(A[i], 1);
        else frequencyMap.update(A[i], frequencyMap.get(A[i]));
    }

    for (int x : Q) {
        if (!frequencyMap.containsKey(x)) print("0");
        else print(frequencyMap.get(x));
    }
}
```

1. Given and integer array of size N. Find the first non repeating element.

```java
int findNonRepeating(int A[]) {
    HashMap<Integer, Integer> frequencyMap = new HashMap<>();
    for (int i=0; i < A.length; i++) {
        if (!frequencyMap.containsKey(A[i]) frequencyMap.insert(A[i], 1);
        else frequencyMap.update(A[i], frequencyMap.get(A[i]));
    }

    for (int i=0; i < A.length; i++) {
        if (frequencyMap.containsKey(A[i] && frequencyMap.get(A[i] == 1))) return A[i];
    }
    throw new Exception("No repeating element");
}

// Time complexity: O(N)
// Space complexity: O(N)
```

1. Given an integer array of size N, find the count of distinct elements.

```
void countDistinct(int A[]) {
    HashSet<Integer> hashSet = new HashSet<>();
    for (int x : A) hashSet.insert(x);
    return hashSet.size();
}

// Time complexity: O(N)
// Space complexity: O(N)
```

1. Given an array of size N, check if there exists a subarray whose sum = 0

```java
// Complete brute force => time complexity O(N^3)
// Carry forward/Prefix sum => Time complexity O(N^2)

/**
 => So in order to reduce the time complexity, we will have to find a way to not calculate the sum of all subarrays. Because if we look at all subarrays, it will take O(N^2)/
 => A technique that allows us to do that is Prefix Sum.

 Sum[i, j] = 0 // Goal of the question
 PS[j] - PS[i-1] = 0 // replace with prefix sum equation
 (Condition => if i==0 then PS[j] = 0)
 PS[j] = PS[i-1] // Simplifying the above equation
*/

boolean subArraySumZero(int A[]) {
    // Build prefix Sum array
    int PS[] = new int[A.length];
    PS[0] = A[0];
    for (int i=1; i < A.length; i++) {
        PS[i] = PS[i-1] + A[i];
        if (PS[i] == 0) return true;
    }
    HashSet<Integer> set = new HashSet<>();
    for (int x : PS) {
        if (set.containsKey(x)) return true;
    }
    return false;
}
```

1. Given the array of size N, count the number of sub arrays with sum = 0

```java
int countSubArrayWithZeroSum() {
    int PS[] = new int[A.length];
    PS[0] = A[0];
    for (int i=1; i < A.length; i++) {
        PS[i] = PS[i-1] + A[i];
    }
}
```

---

## Problems on Hashing

### Two sum

**Problem Statement**  
Given an  integer array of size N and integer K. Check if there exists a pair such that `A[i] + A[j] = K && i != j`

**Brute force**
```java
boolean twoSum(int[] A, int K) {
	for (int i=0; i<A.length; i++) {
		for (int j=0; j<A.length; j++) {
			if (i != j && A[i]+A[j] == K) return true;
		}
	}
	return false;
}
```

**Improving the brute force**
We can observe that to check the pair it order does not matter
i.e `i == j is same as j==i`
So, we can improve the second loop by starting it at `i+1`

```java
boolean twoSum(int[] A, int K) {
	for (int i=0; i<A.length; i++) {
		for (int j=i+1; j<A.length; j++) {
			if (A[i]+A[j] == K) return true;
		}
	}
	return false;
}
```

**Hashing based approach**
```java
boolean twoSum(int[] A, int K) {
	Set<Integer> set = new HashSet<>();

	for (int x : A) {
		if (set.contains(K-x)) return true;
		set.add(x);
	}
	return false;
}
```
**Complexity Analysis**
Time complexity: O(N)
Space complexity: O(N)

### Two sum (count pairs)

**Problem statement**
Given an array of length N, count the sum of pairs that sum up to K.

**Brute force approach**
```java
int countTwoSum(int[] A, int K) {
	int count = 0;
	for (int i=0; i<A.length; i++) {
		for (int j=0; j<A.length; j++) {
			if (i != j && A[i]+A[j] = K) count++;
		}
	}
	return count;
}
```

**HashMap based approach**

Now we need to store the frequency of the elements because answer should be incremented by the frequency of the value `K-A[i]` .
```java
int countTwoSum(int[] A, int K) {
	Map<Integer, Integer> freq = new HashSet<>();
	int count = 0;
	for (int x : A) {
		count += freq.getOrDefault(K-x, 0);;
		freq.put(x, freq.getOrDefault(x, 0)+1);
	}
	return count;
}
```

**Variation**
`(i, j) != (j, i)`
In this case, double the answer from above.

### Sub-array Sum

**Problem Statement**
Given an array of size N. Check if there is a sub-array that sums up to K.

**Brute force**
```java
boolean subArraySum(int[] A, int target) {
	int N = A.length;
	for (int i=0; i<N; i++) {
		for (int j=i; j<N; j++) {
			int sum = 0;
			for (int k=i; k<=j; k++) {
				sum += A[k];
			}
			if (sum == target) return true;
		}
	}
	return false;
}
// Time complexity: O(N^3)
// Space complexity: O(1)

```

**Two loop approach**
We do not need the third loop if we use the carry forward approach [Carry forward](./1-D Array.md)

```java
boolean subArraySum(int[] A, int target) {
	int N = A.length;
	for (int i=0; i<N; i++) {
		int sum = 0;
		for (int j=i; j<N; j++) {
			sum += A[j];
			if (sum == target) return true;
		}
	}
	return false;
}
// Time complexity: O(N^2)
// Space complexity: O(1)

```

**Prefix Sum and HashMap approach**

1. Create a prefix sum array (PS)
2. Find the pair `(x, y)` such that
	1. `x < y && PS[y] - PS[x] = k` => This means sub array does not start at zero
	2. `PS[y] == K` => This means that sub array starts with zero

```java
boolean subArraySum(int A[], int target) {
	int N = A.length;
	int[] PS = new int[N];
	PS[0] = A[0];
	for (int i=0; i<N; i++) {
		PS[i] = PS[i-1] + A[i];
	}
	Set<Integer> set = new HashSet<>();
	for (int x : PS) {
		if (x == 0) return true;
		if (set.contains(target+x)) return true;
		set.add(x);
	}
	return false;
}
```

### Count of distinct elements in Sliding window

**Problem statement**
Given an integer of size N and an integer K.
Find the count of distinct elements in every sliding window of size K.

**Solution using HashMap**
1. Maintain a Frequency HashMap for the sliding window
2. When an element is removed
	1. Reduce the frequency in HashMap
	2. If the frequency becomes 0, remove the key
3. When an element is added.
	1. If the element exists, increase the frequency by 1
	2. If it does not exist, add it.
4. At any point the size of the HashMap gives the count of distinct element in the window

```java
int[] countSlidingWindow(int[] A, int windowSize) {
	int N = A.length;
	int[] ans = new int[N-windowSize+1];
	Map<Integer, Integer> freq = new HashMap<>();

	for (int i=0; i<windowSize; i++) 
		freq.put(A[i], freq.getOrDefault(A[i], 0) + 1);
	ans[0] = freq.size();
	int i = 0, j=WindowSize, k=1;
	while (j < N) {
		freq.put(A[i], freq.get(A[i]));
		if (freq.get(A[i]) == 0) {
			freq.remove(A[i]);
		}
		freq.put(A[j], freq.getOrDefault(A[j], 0) + 1);
		ans[i] = freq.size();
		j++;
		i++;
	} 

	return ans;
}
```