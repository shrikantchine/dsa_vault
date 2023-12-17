# Prime numbers

## Agenda

- Introduction to Prime Numbers
    - Check if a number is prime or not
- Print all prime numbers from 1 to N
    - Sieve of Eratosthenes
- Smallest Prime Factor (SPF)
- Prime Factorization
- Count of Number of Factors/Divisors

## Introduction to prime numbers

- Numbers having exactly 2 factors i.e. 1 and itself.
- 1 is not considered prime number because it does not have 2 factors, it has only one.

✍️ **Check if a given number N, check if it is prime or not.**

```java
boolean isPrime(int N) {
	if (N <= 1) return false;
	for (int i=2; i*i < N; i++) {
		if (N % i == 0) return true;
	}
	return false;
}
```

## Find all prime numbers from 1 to N

Given a number N, print all the prime numbers from 1 to N.

✍️ **Brute force**

- $\forall [1,N]$, check if the count of factor is 2.
- Time complexity: O(n $\sqrt n$)
- Space complexity: O(1)

✍️ **Sieve of Erasthosthenes**

The Sieve of Eratosthenes is an efficient algorithm used to find all prime numbers up to a given limit N. It works by iteratively marking the multiples of each prime number, starting from 2, as composite (i.e., not prime). This process continues until all the numbers up to N have been checked. The numbers that are not marked as composite after this process are prime numbers.

The algorithm can be summarized as follows:

1. Create a boolean array of size N+1 and initialize all the elements as true.
2. Iterate through the array starting from 2.
3. If the current number is marked as true (i.e., prime), then mark all its multiples as false.
4. Repeat steps 2 and 3 until the square of the current number is greater than N.
5. The numbers that are still marked as true in the array are prime numbers.

Using the Sieve of Eratosthenes algorithm significantly improves the efficiency of finding prime numbers compared to the brute force method mentioned earlier.

```java
void sieveOfEratosthenes(int N) {
    boolean[] primes = new boolean[N+1];
		Arrays.fill(primes, true);
		
		for (int i=2; i*i<=N; i++) {
			if (primes[i]) {
				for (int j=i*i; j<=N; j = j+i) {
					primes[j] = false;
				}
			}
		}

		for (int i=2; i<=N; i++) {
			if (primes[i]) {
				System.out.print(i + " ");
			}
		}
}

```

The Sieve of Eratosthenes algorithm has a time complexity of O(N log log N) and a space complexity of O(N).

**How to calculate time complexity ?**

- $\forall [2, \sqrt N]$ ⇒ We iterate over the multiples of it.