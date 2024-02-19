```table-of-contents
```
# 1-D Array

### 💡 Given an array of size N, find the subarray with max sum and return the max sum

### Brute force:

- Iterate in all subarrays
- find the sum of the sub array and keep track of max sum
    
    ```java
    int findMaxSumOfArr(int[] A, int N) {
            ans = A[0]
            for (int i=0; i<N; i++) {
                int sum = 0;
                for (int j=i, j<N; j++) { 
                    for (int k=0; k<=j; k++) sum += A[k];
                }
                ans = Math.max(ans, sum);
            }
            return ans;
        }
    
        //Time complexity: O(N^3)
        //Space complexity: O(1)
    ```
    

### Prefix Sum

- Calculate prefix array
- Use it to remove the 3rd inner loop
- Time complexity reduces to `O(N^2)`
- Space complexity increases to `O(N)`

### Carry forward

- Optimise the inner loop using carry forward as below

```jsx
int findMaxSumOfArr(int[] A, int N) {
        ans = A[0]
        for (int i=0; i<N; i++) {
            int sum = 0;
            for (int j=i, j<N; j++) { 
                sum += A[j];
                ans = Math.max(ans, sum);
            }
        }
        return ans;
    }

    //Time complexity: O(N^2)
    //Space complexity: O(1)
```

### Contribution Technique

- Not possible because it is used when sum of all subarrays
- Here we need max of sum of subarrays

### Improvements = Kadane’s algorithm

Lets consider cases: 
- All elements are positive => Ans is sum of all elements 
- All elements are negative => Ans is largest element in the array OR smallest absolute value in the array 
- If positives are present in between negatives => Sum all positives

```
Example:
A = [-ve, -ve, -ve, -ve, +ve, +ve, +ve, +ve, -ve]
```

- If all positives are on cornors => Ans is sum of all positives

```
Example:
A = [+ve, +ve, +ve, -ve, -ve, -ve] OR [-ve, -ve, -ve, +ve, +ve, +ve]
```

- Mix of positives and negatives
    - Iterate the array and keep two variables
        - `currSum` at index `i` represents the best sum till index i
        - `maxSum` at index `i` represents the best sun overall.
    - If previosly calculate `currSum` is -ve, make it `0`
    - Add `A[i]` to `currSum`
    - Update `maxSum` to be max of `maxSum` and `currSum`

```
Examples:
A = [-ve, +ve, -ve, -ve, -ve, +ve, +ve, -ve, -ve]

Another example:
A        : [-20. 10, -20, -12,  6,  5, -3,  8, -2]
currSum  : [-20, 10, -10, -12,  6, 11,  8, 16, 14] // When current value is -ve and the value encountered is -ve, set currSum = 0
Max Sum  : [-20, 10,  10,  10, 10, 11, 11, 16, 16]

Thus 16 is the ans
```

Code of Kadane’s algorithm

```java
int subArrayMaxSum(int A[], int N) {
    int maxSum = arr[0]; // Can also use Integer.MIN_VALUE
    int currSum = 0;
    for (int i=0; i<N ; i++) {
        currSum += A[i];
        maxSum = Math.max(maxSum, currSum);
        if (currSum < 0) currSum = 0;
    }
}

// Time complexity: O(N)
// Space Complexity: O(1)
```

### 💡 Given an array of size N, find the subarray with min sum and return the min sum

- Multiply all values with -ve and run kadane’s algorithm

### 💡 Given an array of size N, find the subarray with max sum and return the subarray itself.

- Keep track of left and right index for both maxSum and currSum

### 💡 Given an integer array A of size N, where every element is zero, return final array after performing multiple queries as below

- Query(i, x) => Add x to all numbers from i to N-1

```
Example:  N = 7
    A   : [0, 0, 0, 0, 0, 0, 0]
Q(1, 3) : [0, 3, 3, 3, 3, 3, 3]
Q(4, 2) : [0, 0, 0, 0, 2, 2, 2]
Q(3, 1) : [0, 0, 0, 1, 1, 1, 1]
------------------------------------
   ANS  : [0, 3, 3, 4, 6, 6, 6]
```

### Brute force approach:

- Do all queries one by one and update the same array
- Time complexity: `O(Q*N)`
- Space complexity: `O(1)`

### Aggregate the queries => Lazy sum algorithm

- For each query, update only the index mentioned in the query
- Use prefix sum to propagate the sum => return the prefix sum

```java
void solve(int[] A, int[][] query) {
    // Aggregate the query
    for (int[] x : query) {
        A[x[0]] += x[1];
    }
    // Calculate prefix sum
    for (int i=1; i<A.length; i++) {
        A[i] = A[i-1] + A[i];
    }
    System.out.println(Arrays.toString(A));
}

// Time complexity: `O(Q+N)`
// Space complexity: `O(1)`
```

### 💡 In the prev question, the query is modified as below

### Query(i, j, x) => Add x to all numbers from i to j

- Brute force: For each query, iterate from i to j and add x to array
    - Time complexity: `O(N*Q)`
    - Space complexity: `O(1)`
- Lazy sum:
    - Since lazy sum does to stop at any index j
    - We need to do something to neutralize the effect of adding the value x to after the index j for each query.
    - This implies `Q(i, j, x) => Q(i, x) & Q(j+1, -x)`

```java
void solve(int[] A, int[][] query) {
    // Aggregate the query
    for (int[] x : query) {
        A[x[0]] += x[2];
        if (x[i] < N-1) 
            A[x[1]+1] -= x;
    }
    // Calculate prefix sum
    for (int i=1; i<A.length; i++) {
        A[i] = A[i-1] + A[i];
    }
    System.out.println(Arrays.toString(A));
}
```

### 💡 Rain water trapping problem

### Given N buildings with height of each building, find the rain water trapped between the buildings

- [Leetcode reference](https://leetcode.com/problems/trapping-rain-water/description/)

### Observations 1: We have taller building on both sides

At any index i - Find the tallest building on left `l` - Find the tallest building on right `r` - Water at index i = `Min(l, r) - A[i]`

### Observation 2: Building at current index is has no taller building on either side

- Ans = 0

### Brute force solution

- For every building
    - find left max
    - find right max
    - calculate water units

```java
void calculateRainWater(int[] A, int N) {
    ans = 0;
    for (int i=1; i<N-1; i++) {
        int maxL = 0, maxR = 0;
        for (int j=0; j < i; j++) {
            maxL += A[i];
        }
        for (int j=i+1; j < n; j++) {
            maxR += A[i];
        }
        int water = Math.min(maxL, maxR) - A[i];
        if (water > 0) ans += water;
    }
}

// TC: O(N^2)
// SC: O(1)
```

### Optimize TC: Use prefix and suffix max array

```
Example:

         [8, 6, 4, 7, 5, 9, 8, 3]
lMax  :  [8, 8, 8, 8, 8, 9, 9, 9] //Prefix sum array
rMax  :  [9, 9, 9, 9, 9, 9, 8, 3] //Suffix Sum array
---------------------------------------
Water :  [0, 2, 4, 1, 3, 0, 0, 0] //min(lMax[i], rMax[i]) - A[i] OR zero if the value is -ve
```

```java
void calculateRainWater(int[] A, int N) {
    int lMax[] = new int[N];
    int rMax[] = new int[N];
    int ans = 0;

    for (int i=1; i<N; i++) lMax = Math.max(A[i], lMax[i-1]);
    for (int i=N-2; i>=0; i--) rMax = Math.max(A[i], lMax[i+1]);

    for (int i=1; i<N; i++) {
        int water = Math.min(lMax[i-1], rMax[i+1]) - A[i];
        if (water > 0) ans += water;
    }
}
```

### Carry forward

- Carry forward cannot be used for both suffix and prefix array simulataneously.
- So, we can use carry forward for either prefix or suffix array

```java
void calculateRainWater(int[] A, int N) {
    int rMax[] = new int[N];
    int ans = 0, lMax = A[0];

    for (int i=N-2; i>=0; i--) rMax = Math.max(A[i], lMax[i+1]);

    for (int i=1; i<N; i++) {
        int water = Math.min(lMax, rMax[i+1]) - A[i];
        if (water > 0) ans += water;
        lMax = Math.max(lMax, A[i]);
    }
}
```

### Two pointer approach

Observations: To calculate the value of water units at any index i, we need lMax and rMax

## 💡**Maximum Absolute Difference**

### Problem statement:

Given an array of size N, find the max value of |A[i] - A[j]| - |i-j|

### Brute force

```jsx
int absoluteDifferece(int[] A) {
	int ans = Integer.MIN_VALUE;
	for (int i=0; i<A.length; i++) {
		for (int j=0; j=A.length; j++) {
			ans = Math.max(ans, Math.abs(A[i] - A[j]), Math.abs(i-j));
		}
	}
	return ans;
}

// TC: O(N*2)
// SC : O(1)
```

### Observations

1. Since i-j is same as j-i when the absolute values is considered. We do not need to consider these cases twice. Therefore, we can check all values where i > j without loosing any solution. Thus the expression becomes
    
    <aside>
    💡 |A[i]-A[j]| - (i-j)
    
    </aside>
    
2. Now we can consider two cases
    1. A[i] > A[j]
    
    <aside>
    💡 (A[i] - A[j]) - (i-j)  ⇒ (A[i] + i) - (A[j] + j)
    
    </aside>
    
    1. A[i] ≤ A[j]
    
    <aside>
    💡 (A[j] - A[i]) - (i-j)  ⇒ (A[j]-j) - (A[i] - i)
    
    </aside>
    

Thus above equations establish relation between the value and its indices. We can use that to write code as below

### O(N) space solution

1. Construct an array B[i] = A[i] - i
2. Construct an array C[i] = A[i] - i
3. Take the max(max(B[i] - min(B[i]), max(C[i] - min(C[i]))

```jsx
int absoluteDifference(int[] A) {
	int N = A.length;
	int[] B = new int[N];
	int[] C = new int[N];
	for (int i=0; i<A.length; i++) {
		B[i] = A[i] - i;
		C[i] = A[i] + i;
	}
	int ans1 = getMax(B) - getMin(B);
	int ans2 = getMax(C) - getMin(C); 
	return Math.max(ans1, ans2);
}

int getMin(int arr[]) {
       return Arrays.stream(arr).min().getAsInt();
 }
 
static int getMax(int arr[], int n) {
      return Arrays.stream(arr).max().getAsInt();
}
```

### O(1) space solution

1. Calculate min and max in the first loop without storing them in the array.

```java
int absoluteDifference(int[] A) {
	int N = A.length, minB = Integer.MAX_VALUE, minC = Integer.MAX_VALUE, maxB = Interger.MIN_VALUE, maxC = Integer.MAX_VALUE;
	
	for (int i=0; i<A.length; i++) {
		minB= Math.min(minB, A[i] - i);
		minC= Math.min(minC, A[i] + i);
		maxB= Math.max(maxB, A[i] - i);
		maxC= Math.max(maxC, A[i] + i);
	}
	int ans1 = maxB - minB;
	int ans2 = maxC - minC; 
	return Math.max(ans1, ans2);
}
```