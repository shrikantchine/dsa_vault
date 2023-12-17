# Prefix Sum/Carry forward/Sliding Window

# Prefix Sum

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

# Carry forward

The basic idea behind this technique is to keep track of previsouly calculate values and use it to calculate the next values.

For example, while calculating the maximum value from an array, naive approach is to compare each value with all other values. This can be optimized by keeping track of the maximum value seen so far and check that against the current value to see if any value exists that is can be greater than already seen value.

In this way, we are carrying forward the max value that we have seen so far.

# Sliding Window

- Window Sliding Technique is a computational technique that aims to reduce the use of nested loops and replace it with a single loop, thereby reducing the time complexity.
- Size of the window should be fixed
- The general use of the Sliding window technique can be demonstrated as follows:
    - Find the size of the window required
    - Compute the result for 1st window, i.e. from the start of the data structure
    - Then use a loop to slide the window by 1, and keep computing the result window by window.

# Questions

- ✔️Find equilibrium point of an array (Prefix sum and carry forward) [Code](./src/prefix_sum/EquilibriumPoint.java)
- ✔️Maximum sum subarray of size k [Code](./src/prefix_sum/MaxSumSubArr.java)