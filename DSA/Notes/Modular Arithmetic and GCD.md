# Modular Arithmetic and GCD

## ✔️ What is modular Arithmetic ?

- Consider the following equation

<aside>
💡 D = q * d + r

</aside>

Where:

D ⇒ Dividend

q ⇒ Quotient

d ⇒ Divisor

r ⇒ Remainder

- For many DSA questions, return value is A%B. This limits the value that is returned to
    
    <aside>
    💡 0 ≤ A%B ≤ B-1
    
    </aside>
    

## ✔️ Operation

- **(a + b) % m  = (a%m + b%m) % m**
    
    To prove that (a + b) % m = (a % m + b % m) % m, we can use the properties of modular arithmetic.
    
    Let's assume:
    a = q1 * m + r1
    b = q2 * m + r2
    
    where q1, q2 are quotients and r1, r2 are remainders.
    Now, we can substitute these values into the equation (a + b) % m:

    (a + b) % m = (q1 * m + r1 + q2 * m + r2) % m
    
    Using the properties of modular arithmetic, we can distribute the modulo operator:
    
    = ((q1 * m) % m + r1 % m + (q2 * m) % m + r2 % m) % m
    
    Since (q1 * m) % m and (q2 * m) % m are both equal to 0, we can simplify the equation to:
    
    = (r1 % m + r2 % m) % m
    
    which can be further simplified to:
    
    = (a % m + b % m) % m
    
    Therefore, we have proved that (a + b) % m = (a % m + b % m) % m.
    
- **(a * b) % m  = (a%m * b%m) % m**
- **(a - b) % m  = (a%m - b%m + m) % m**
- **((a%m)%m)%m… = a % m**
- **(a^b)%(m)  = (a % m)^b % (b)**

## ✔️ Question

- **Problem statement**

Given an integer array, find the count of pairs (i, j) such that (A[i] + A[j]) % m == 0. (i, j) is same as (j, i)

- **Brute force**
1. For all i, j, check and count if (A[i] + A[j]) % m == 0
2. Time complexity: O(N^2)
3. Space Complexity: O(1)

- **Optimized**

$(A[i] + A[j]) mod M = 0$ 

⇒ $(A[i]modM + A[j]modM)modM=0$ 

1. A[i] mod M ranges from (0 - M-1)
2. So, to make (A[i]modM + A[j]modM)modM zero, the value of (A[i]modM + A[j]modM) should be either zero or M.
3. So, the solution is find the pairs that add up to M and those that add up to zero.
4. Pairs that add up to zero = $nC2 => n*(n-1)/2$ where n is the number of zeros in the above array

```java
void modSum(int[] A, int M) {
	int[] freq = new int[M];

	for (int i=0; i<A.length; i++) {
		A[i] = A[i] % M;
		freq[A[i]] = freq[A[i]] + 1;
	}

	int ans = freq[0] * (freq[0] - 1) / 2;

	for (int i=0; i<A.length; i++) {
		if (A[i] != 0) {
			int x = M - A[i];
			ans += freq[x];
		}
	}

	return ans;
}
```

