
```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
## Things to remember

### ✔ How many numbers in the range [a, b]

`b-a+1`

### Arithmetic progression

Defined as a series where difference between two consecutive elements is same. Formula to calculate the sum

`(n) * (n+1)/2`

### Geometric progression

A geometric progression is a sequence in which any element after the first is obtained by multiplying the preceding element by a constant called the common ratio which is denoted by r

```
sum = a * (r^N - 1) / (r-1)
    where a = first element
          r = common ratio
    condition: r != 1
```

## Scientific Notation

In java, scientific notations are a way to represent floating point literals. It allows you to represent a number as a coefficient and power of 10. The general form is

```
mEn or men => m * 10^n
    m is called mantissa or coefficient
    n is called exponent

Example:
    2e2 = 2 * 10^2 = 200
    1e2 = 1 * 10^2 = 100
    10e2 = 10 * 10^2 = 1000
```

## Handling input constraints in DSA problems

- A typical 1Ghz computer handles 109 iterations per second. As a standard, 1Ghz CPU is allocated by Online plateforms like Leetcode
    
    8-10
    
- Online plateforms require that the code is executed in 1sec.
- So, based on the range of expected iterations, what should be the time complexity ?

| Number of iterations | Valid time complexities |
| --- | --- |
| N <= 10^6 or 1e6 or 10e5 | O(N), O(NLogN) |
| N < 20 | O(N), O(N^2), O(N^3), O(2^N) |
| 10^10 >= N > 10^9 | O(log n), O(sqrt n) |

## Prime vs Composite numbers

| Prime numbers | Composite number |
| --- | --- |
| Natural number greater than 1 and divisible by 1 and itself | A number greater than 1 that is not a prime number |
- [How to find if a number is prime ?](./../src/math/IsNumberPrime.java)
- [Find all prime number below given integer n](../src/math/SieveOfEratosthenes.java)
- [Find if a number is composite](../src/math/IsCompositeNumber.java)

## What is an identity value ?

Identity of any operation is defined as any CONSTANT value that does not change the value upon the application of that operation.

Example:

- a + 0 = a ⇒ 0 is the identity value for summation operation
- a - 0 = a ⇒ 0 is the identity value for subtraction operation

## GCD and LCM

s

## How to solve recursion/DP problems

[[Dynamic Programming#Staircase]]

## 🌟 Important Links

- 💡[yangshun tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook)
- 💡[Typing practice](https://www.keybr.com/)
- 💡[Competitive programming handbok](https://cses.fi/book/book.pdf)
- 💡[System design 101](https://github.com/ByteByteGoHq/system-design-101)