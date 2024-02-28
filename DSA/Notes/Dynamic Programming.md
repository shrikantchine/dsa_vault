```table-of-contents
```

## Introduction to dynamic programming

### Fibonacci Series

The following is the recursive definition of Fibonacci series

$$
f(n) = 
\begin{cases}
   0 &\text{if } n=0 \\
   1 &\text{if } n=1 \\
   f(n-1) + f(n-2) &\text{if } n>1
\end{cases}
$$

- To solve this using recursion, we will use repeating sub problems 
- For example:  to calculate `fib(5)` -> we will call `fib(3)` two times, `fib(2)` three times.

### When to use dynamic programming

- In order to use Dynamic programming, there are 2 requirements
	- A problem has optimal substructure.
		- A problem has optimal substructure if we are recursively solving.
	- The problem has overlapping sub problems.
		- Repeating sub problems


### Memoization

- Storing the value of a sub problem that we encounter and using it when we encounter the same sub problem in a future encounter
- Example: To calculate `fib(N)`, use an array of size `N+1` elements where `arr[i]` stores the `fib(i)`

```java
int fib(N) {
	int[] memo = new int[N+1];
	Arrays.fill(memo, -1);
	return helper(N, memo);
}

int helper(int N, int[] memo) {
	if (N == 0 || N == 1) {
		memo[N] = N;
		return N;
	}
	if (memo[N] != -1) return memo[N];
	memo[N] = helper(N-1) + helper(N-2);
	return memo[N];
}
```

**Time complexity**
Time complexity: O(n)
Space complexity:  O(n) for recursion stack + O(n) for memoization $\approx$ O(n)


## Ways to solve dynamic programming problems

### Top down dynamic programming

- Recursion + Memoization = Top down approach
- We start with a bigger problem
- Go down recursively to a smaller sub problem for which we already know the answer (Base case)
- Implemented for `fib(N)` above

### Bottom up dynamic programming (Tabulation)

- Iterative approach instead of recursion
- Start from the smallest sub problem (Base case)
- Use it in iterative approach to solve the bigger problem

```java
int fib(N) {
	int[] arr = new int[N+1];
	arr[0] = 0;
	arr[1] = 1;
	int i = 2;
	while (i != N) {
		arr[i] = arr[i-1] + arr[i-2];
	}

	return arr[N];
}
```

**Time complexity**
Time complexity: O(n)
Space complexity:  O(n)

### Comparison

| # | Bottom Up | Top Down |
| ---- | ---- | ---- |
| 1 | Less intuitive | More intuitive |
| 2 | More space efficient (No stack space) | Less space efficient |
| 3 | More control | Less Control (No control over how the recursive state is calculated or how the function is called) |
> More control = More optimisation
> Example below

```java
int fib(N) {
	int n1 = 0;
	int n2 = 1;
	int i = 2;
	while (i != N) {
		int tmp = n1 + n2;
		n2 = n1;
		n1 = tmp;
	}

	return n1;
}
```

**Time complexity**
Time complexity: O(n)
Space complexity:  O(1)

### DP State

`DP[i] `: What are we calculating at `ith` step

### Staircase 

**Problem Statement**

Given staircases numbered from 0 to N. In 1 step, you can jump 1 stair or 2 stairs.
Find the number of ways to reach Nth staircase.

**Example**
N = 1 => 1
N = 2 => 2
N = 3 => 3

**Solution**
> Notion of choice = Recursion in most cases

**Steps to solve Recursion/DP problems**
1. Identify the element of choice. In this example: 1 step or 2 step in each iteration
2. Represent the state. In this example: DP[i] = No of ways to reach ith step.
3. Use step 1 and step 2 to write recurrence relationship.
	$$
		DP[n] = 
		\begin{cases}
		   1 &\text{if } n=0 \\
		   2 &\text{if } n=1 \\
		   DP[n-1] + DP[n-2] &\text{if } n>1
		\end{cases}
	$$
4. Identify the state which is the final answer: In this case: DP[N]
5. Identify if DP can be applied
	1. Overlapping sub problems => In our case, they are present. 
	2. Optimal sub structure => In our case, it is present
6. Top Down DP vs Bottom up DP
	1. Top Down: Use memoization
	2. Bottom up: Use two variables to hold previous two steps.


```java
int countWays(int n) {
	int n0 = 1;
	int n1 = 2;

	for (int i=2; i<=n; i++) {
		int tmp = n0 + n1;
		n1 = n0;
		n0 = tmp;
	}

	return n0;
}
```

### Perfect Square Sum

**Problem statement**

Given an integer N, Figure out the minimum number of perfect squares we can add to get the sum = N.

**Examples**

```text
N = 6
Way 1 => 1 + 1 + 1 + 1 + 1 + 1
Way 2 => 4 + 1 + 1

Therefore: Way 2 gives minimum number of perfect squares
Ans = 3
```

**Why greedy cannot be implemented**

Greedy solution
- Find the nearest perfect square to given number
- Subtract it from number and do the same steps again.

It does not work for N = 12
- Greedy gives ans = 4
- Correct ans is 3

**What happens if greedy fails**

- The only alternative is to explore all choices Or Brute force
- So, for this example
	$\forall i$ 

**Solution**

1. Elements of choices => $\forall \space i \space where \space i*i <= N$
2. Represent State => DP[i] = Min Squares required for for sum = N
3. Recurrence relation => 
$$
			DP[n] = 
		\begin{cases}
		   1 &\text{if } n=0 \\
		   2 &\text{if } n=1 \\
		   \forall j &  j*j < n&min(DP[i-j^2]) &\text{if } n>1
		\end{cases}
$$
4. Which state is the answer ?
	- We can use an array of size `N+1`
	- Because in the branch where 1 is the perfect square always, we will have all states from N to 1

```java
int minSquareSum(int N) {
	int[] dp = new int[N+1];
	dp[0] = 0;
	dp[1] = 1;
	for (int i=2; i<=N; i++) {
		dp[i] = i;
		for (int j=2; j*j<=i; j++) {
			dp[i] = Math.min(dp[i], 1 + dp[i-(j*j)]);
		}
	}
	return dp[N];
}
```

### Maximum sum without adjacent elements

**Problem statement**
Find the max sub sequence sum from a given integer array of size N where you cannot select adjacent elements.

**Example**
```
A = [9, 4, 13]
Max sub sequence sum = 22 (By selecting elements 9 and 13)

A = [9, 4, 13, 24]
Max sub sequence sum = 33 (By selecting elements 9 and 24)
```

#### Brute force
- Generate all valid sub-sequences and get max of them
- How to generate ?
	- Select/not select an element and solve the remaining elements as a sub problem
- Should we start from left or right ?
	- Right is better because for the remaining sub problem, the indexes start again from 0.
- At each recursion state, we need to pass whether or not the previous element was selected or not. This needs to be passed into the recursion stack.

> [!NOTE] When to use backtracking vs DP optimization
> If the outcome of the function is passed as input argument, then we use backtracking. 
> If the outcome of the function is returned from the function, then we can use DP optimization 

**Backtracking solution**

- Should be used when the it is asked to generate all possible solution

```java
int ans = 0; //Global variable
void maxSum(int[] A, int idx, boolean lastSelected, int sum) {
	if (idx == -1) {
		ans = Math.max(ans, sum);
		return;
	}
	maxSum(A, idx-1, false, sum); // Choice to not select current element
	if (lastSelect == false) {
		maxSum(A, idx-1, true, sum+A[i]); // Choice to select current element
	}
}
```

**Solution if the function returns the answer of sub problem**

```java
int findMaxSum(int[] A) {
	return maxSum(A, A.length-1, false);
}
int maxSum(int[] A, int idx, boolean isPrevSelected) {
	if (idx < 0) return 0;
	if (isPrevSelected) return maxSum(A, idx-1, false);

	int sumWithSelection = maxSum(A, idx-1, true) + A[idx];
	int sumWithoutSelection = maxSum(A, idx-1, false);

	return Math.max(sumWithSelection, sumWithoutSelection);
}
```

**Complexity analysis**
- Time Complexity: O(2^n) => In both cases

#### Dynamic Programming

*State*:  `maxSum(i)` => Represents the maximum out of elements from 0 to u

*Recursion Relationship*:

$$
maxSum[i] = max
		\begin{cases}
		   maxSum(i-2) + A[i] &\text{if selected} \\
		   maxSum(i-1) &\text{if not selected} \\
		\end{cases}
$$

*Base case*:
Base case is when the above recurrence relationship provide invalid results.

| i   | i-1 | i-2 | is base case | What to return in the base case ? |
| --- | --- | --- | ------------ | --------------------------------- |
| 0   | -1  | -2  | Yes          | A[0]                              |
| 1   | 0   | -1  | Yes          | max(A[0], A[1])                   |
| 2   | 1   | 0   | No           |                                   |
*Which state is the answer?*
maxSum(N-1)

```java
int findMaxSum(int[] A) {
	return maxSum(A, A.length-1);
}

int maxSum(int[] A, int idx) {
	if (idx == 0) return A[0];
	if (idx == 1) return Math.max(A[0], A[1]);
	return Math.max(maxSum(A, idx-1), maxSum(A, idx-2) + A[i]);
}
```

**Adding dynamic programming**

- Top Down approach (Using memoization) 

```java
int findMaxSum(int[] A) {
	int[] dp = new int[A.length];
	Arrays.fill(dp, -1);
	return maxSum(A, A.length-1, dp);
}

int maxSum(int[] A, int idx, int[] dp) {
	if (idx == 0) return A[0];
	if (idx == 1) return Math.max(A[0], A[1]);
	if (dp[idx] == -1) return dp[idx];
	dp[idx] = Math.max(maxSum(A, idx-1, dp), maxSum(A, idx-2, dp) + A[i]);
	return dp[idx];
}
```

**Complexity Analysis**
Time complexity: O(n)
Space Complexity: O(n) for array + O(n) for stack => O(n)

- Bottom up approach

```java
int findMaxSum(int[] A) {
	int[] dp = new int[A.length-1];
	dp[0] = A[0];
	dp[1] = Math.max(A[0], A[1]);

	for (int i=2; i<A.length; i++) {
		dp[i] = Math.max(dp[i-1], A[i], d[[i-2]]);
	}

	return dp[A.length-1];
}
```

**Complexity Analysis**
Time complexity: O(n)
Space Complexity: O(n)

- Removing the extra space

```java
```java
int findMaxSum(int[] A) {
	int[] dp = new int[A.length-1];
	dp1 = A[0];
	dp2 = Math.max(A[0], A[1]);
	int result = Math.max(dp1, dp2);

	for (int i=2; i<A.length; i++) {
		result = Math.max(dp1, dp2+A[i]);
	}

	return dp2;
}

```

**Complexity Analysis**
Time complexity: O(n)
Space Complexity: O(1)

## Two dimensional dynamic programming

- Up until now, there was only 1 variable that was defining the recursive state. That's why we were able to store states in 1-D array
- If the recursive state is two dimensional, it is called 2-D dynamic programming
- States are stored in 2-D matrix.
- Two types are DSA problem statements exist here
	- Grid problems: Input is `N*M` matrix.
	- Other problems: We identify the two parameters that define the state, and build DP matrix

### Count unique paths

#### Problem Statement
Given a matrix of size `N*M`. Find the total number of ways to go from `(0, 0)` to `(N-1, M-1)`
You are allowed to move right `i, j -> i+1, j` and down `i, j -> i, j+1`.

#### Solution

- Notion of choice: We have choice to move left or right. Therefor recursion can be a solution
- Elements of Choice
	- Go right
	- Go down
- State definition: `Ways(i, j)` can be defined as ways to reach cell `(i, j)` from `(0, 0)`
- Recurrence relation: 
	$$
	ways[i][j] = \sum
		\begin{cases}
		   ways[i-1][j] &\text{Coming from left} \\
		   ways[i][j-1] &\text{Coming from top} \\
		\end{cases}
	$$
- Base Cases:
	- Base case is when an invalid state is produced in recurrence relation
	- Therefor i=0 OR j=0 are the base cases.
	- It makes sense, since there is only 1 way to reach any cell in first row or column.
- How to find the answer?
	- `ways[N-1][M-1]` is the answer

```java
int findWays(int[][] A) {
	int N = A.length;
	int M = A[0].length;
	return ways(A, N-1, M-1);
}

int ways(int[][] A, int i, int j) {
	if (i==0 || j==1) return 1;
	return ways(A, i-1, j) + ways(A, i, j-1)
}
```

- Since there are overlapping sub-problems here, DP can be applied.

**Top Down approach (Memoization)**

- Add a DP array of size `N*M`

```java
int findWays(int[][] A) {
	int N = A.length;
	int M = A[0].length;
	int[][] dp = new int[N][M];
	for (int[] arr : dp) Arrays.fill(arr, -1);
	return ways(A, N-1, M-1, dp);
}

int ways(int[][] A, int i, int j, int[][] dp) {
	if (i==0 || j==1) {
		dp[i][j] = 1;
		return dp[i][j];
	}
	if (dp[i][j] != -1) return dp[i][j];
	dp[i][j] = ways(A, i-1, j) + ways(A, i, j-1)
	return dp[i][j];
}
```

**Complexity Analysis**
Time complexity: `O(n*m)`
Space Complexity: `O(n*m)`


**Bottom Up approach**

```java
int findWays(int[][] A) {
	int N = A.length;
	int M = A[0].length;
	int[][] dp = new int[N][M];

	for (int i=0; i<N; i++) {
		for (int j=0; i<M; j++) {
			if (i == 0 || j == 0) {
				dp[i][j] = 1;
			}
			else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1];
			}
		}
	}
	return dp[N-1][M-1];
}
```

**Complexity Analysis**
Time complexity: `O(n*m)`
Space Complexity: `O(n*m)`

**Reducing the space complexity**
Since we only need 1 previous array, we can just work with 2 arrays

```java
int findWays(int[][] A) {
	int N = A.length;
	int M = A[0].length;
	int[][]dp = new int[2][M];

	for (int i=0; i<N; i++) {
		for (int j=0; i<M; j++) {
			if (i == 0 || j == 0) {
				dp[1][j] = 1;
			}
			else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1];
			}
		}
	}
	return dp[N-1][M-1];
}
```

## Knapsack problems

Knapsack is a category for problem where we are given 2 types of arrays V & W where 

V[i] => Representing the profit/loss value of ith item
W[i] => Representing the weight value of ith item

A bag with capacity `C` is given. Select objects such that W[i] <= C but sum of profit/loss is maximised or minimised

### Fractional knapsack

**Problem Statement**

Given N cakes. Each cake has a happiness value given by array H and weight value represented by array W.
You visit the bakery with bag of capacity C. Find the max value of happiness that you can carry in the bag.

Note: Cake can also be divided. 

**Solution**
- We can approach this greedily by selecting the items in the decreasing order of happiness per unit weight until the bag is full.

So, to solve this
- Sort the objects w.r.t. H[i]/W[i]
- Select the cakes in decreasing order & remaining capacity

**Complexity Analysis**
Time complexity: O(n log n) ==> Sorting
Space complexity: O(n)

### 0-1 Knapsack

Given N toys. Each toy has a happiness value given by array H and weight value represented by array W.
You visit the bakery with bag of capacity C. Find the max value of happiness that you can carry in the bag.

Note: Toy can't be divided. 

**Observations**
- Greedy approach is not possible here.
- So, when greedy fails, the only option left is to perform brute force using recursion and find a way to optimize using DP (if possible)


DP Solution:
	- Element of Choice: Purchase or not
	- State: happiness(i, c) represents max happiness that we can obtain if we select elements from [0, i] with capacity C
	- Recurrence Relationship
	$$
		happiness(i, j) = 
		max
		\begin{cases}
		   happiness(i-1, j-w[i]) + H[i] &\text{if selected} \\
		   happiness(i-1, j) &\text{if not selected} \\
		\end{cases}
	$$

	- Which state is the answer ?
	happiness(N-1, C)

```java
int maxHappiness(int[] H, int[] W, int C) {
	return helper(H, W, C, H.length-1);
}

int helper(int[] H, int[] W, int C int idx) {
	if (idx < 0) return 0;
	if (C == 0) return 0;
	int answer = helper(H, W, idx-1);
	if (W[idx] <= C) {
		answer = Math.max(answer, helper(H, W, C-W[idx], idx-1));
	}
	return answer;
}
```

**Complexity**
Time complexity: O(2^N)

- Do we have overlapping sub-problems ?
	- YES => Can be checked by building the recursion tree for some example.

**DP solution**

- We will use 2-D DP matrix where rows represent index and columns represent capacity
- Base cases
	- Index = -1
	- Capacity = 0
- Since base case cannot be stored in DP array DP array size should be N+1, C+1
- This means that index `i` in DP represents `i-1`th index in Happiness array

```java
int maxHappiness(int[] H, int[] W, int C) {
	int N = H.length;
	int[][] dp = new int[N+1][C+1];

	for (int i=1; i<=N; i++) {
		if (j=1; j<=C; j++) {
			if (W[i-1] <= j) {
				dp[i][j] = Math.max(dp[i-1][j] + H[i-1], dp[i-1][j-W[i-1]);
			} else {
				dp[i][j] = dp[i-1][j];
			}
		}
	}
	return dp[N][C];
}
```

**Complexity**
Time complexity: `O(N*C)`
Space complexity: `O(N*C)`


### 0-N or Unbounded Knapsack

- Unlimited supply of each item is present.
- In 0-1 knapsack, after processing the element (select or reject), the element is considered processed and cannot be selected again.
- In 0-N knapsack, if we reject the element, it is considered processed but if we select an element, it is not considered processed because we can process it again.
- So the recurrence relationship is

$$
		happiness(i, j) = 
		max
		\begin{cases}
		   happiness(i, j-w[i]) + H[i] &\text{if selected} \\
		   happiness(i-1, j) &\text{if not selected} \\
		\end{cases}
	$$
- Same code as 0-1 knapsack can be used with small change to recurrence relation is described

How to reduce it to 1-D DP problem ?

- dp[i] => Max happiness in a bag with capacity `i`
- Recursive relation
	$$
	dp[i] = max(\forall object \text{ (H[obj] + dp[i-w[obj]]) } if w[obj] <= i)
	$$

```java
int maxHappiness(int[] H, int[] W, int C) {
	int N = H.length;
	int[] dp = new int[C+1];

	for (int i=1; i<=C; j++) {
		int maxHappinesss = 0;
		for (int j=0; i<N; j++) {
			if (W[j] <= i) {
				int happiness = H[j] + dp[i-W[j]];
				maxhappiness = Math.max(happiness, maxHappiness);
			}
		}
		dp[i] = maxHappiness;
	}
	return dp[C];
}
```

**Complexity**
Time complexity: `O(N*C)`
Space complexity: `O(C)`