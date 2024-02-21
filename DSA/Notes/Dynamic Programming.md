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
   f(n-1) + f(n-2) &\text{if } n=0
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
