```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
maxLevel: 0 # Include headings up to the speficied level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# 🌟Decimal number system

Available digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

- These digits are unique symbols used in the number systems.
- Total number of unique symbols in any number system is known as the `base of the number system`
- Base of decimal number system is `10`
- How does it work ?

```
// Base gets multiplied to each symbool to generate any number
342 = 300 + 40 + 2 = 3*10^2 + 4*10^1 + 2
```

- In the octal number system, the available symbols are [0, 1, 2, 3, 4, 5, 6, 7]
- To convert value from octal in decimal

```
(1067) as base 8 = 1*8^3 + 0*8^2 + 6*8^1 + 7*8^0
     => the returned value is in decimal number system
     => why does this work? because when we calculate power or addition, we are following the rules of decimal number system
```

- Hexadecimal number system = `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]`

# 🌟Binary number system

- Base = 2
- Symbols = [0, 1] => they are called as bits
- Exmple:

```
1011 (binary) => 1*2^3 + 0*2^1=2 + 1*2^1 + 1*2^0 = 11 (in decimal system)
```

- Decimal to binary

| Divide by | Decimal Number | Remainder |
| --- | --- | --- |
| 2 | 45 | 1 |
| 2 | 22 | 0 |
| 2 | 11 | 1 |
| 2 | 5 | 1 |
| 2 | 2 | 0 |
| 2 | 1 | 1 |
| 2 | 0 |  |

So going up in the remainder, the binary representation of `45` is `101101`

## ✔️Addition of binary numbers

Rules:

- Sum the two digits as decimal numbers
- Positional values would be `result%base`
- Carry will be `result/base`
- Example:
    - 1 + 1 = 2 => (2%2)=0 is the value & 2/2=1 is the carry
    - 1 + 0 = 1 => (1%2)=1 is the value & 1/2=0 is the carry
    - 0 + 0 = 0 => (0/2)=2 is the value & 0/2=0 is the carry

```
    1 0 1 0 1
+     1 1 0 1
-----------------
  1 0 0 0 1 0
```

## ✔️Bitwise operators

Different names for bits

- 0 => False/unset
- 1 => True/set

### NOT (~)

Converts the `0` bit to `1` and vise versa

```
~ 0 = 1
~ 1 = 0
```

### AND (&)

- The result of the AND operator is 1 when all the bits are 1.

| A | B | Result |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
- Example:

```
   5 => 1 0 1
&  6 => 1 1 0
----------------
   4 => 1 0 0
```

- How does it work in code ?

```
int x = 5;
int y = 6;
print(x & y);
```

### OR (|)

- The result of the OR operator is 1 when any one of the bits is 1

| A | B | Result |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |
- Example:

```
   5 => 1 0 1
|  6 => 1 1 0
----------------
   7 => 1 1 1
```

- How does it work in code ?

```
int x = 5;
int y = 6;
print(x | y);
```

### XOR (^)

- Also called as Exclusive OR.
- The result is true only when exactly 1 bit is true

| A | B | Result |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
- Example:

```
   5 => 1 0 1
^  6 => 1 1 0
----------------
   3 => 0 1 1
```

- How does it work in code ?

```
int x = 5;
int y = 6;
print(x ^ y);
```

## ✔️Binary representation of negative number

**Note:** For simplicity lets assume that integers have 5 bits

- 🥏 Most significant bit: Highest order bit in a binary integer
- 🥏 Least significant bit: the binary 1s place of the integer

### Using MSB to represent -ve numbers

MSB is used as sign bit. - The value `1` represents `-ve` numbers - The value `0` represents `+ve` numbers

Problems with this method of representation: - Negative and positive numbers do not add up to zero `10 :   0 1 0 1 0    - 10 :   1 1 0 1 0    ----------------------       0 : x 0 0 1 0 0       // X represents extra bit that cannot be filled in 5 bit integer. Thus ignored.` - Zero and Negative zero have different binary representations `0 : 0 0 0 0 0    -0 : 1 0 0 0 0`

### 2’s compleiment representation

### How to compute negative number’s representation:

- Calculate 1’s complement of the positive number
- Add one to it

### How to calculate 1’s complement

- In the binary representation of a number, replace zeros to one’s and one’s to zeros OR
- Programmatically as below

```java
void onesComplement(int x) {   
	// Find number of bits in X.   
	int numberOfBits = Math.floor(Math.log(x) / Math.log(2)) + 1;   
	// XOR with Math.pow(2, numberOfBits)-1   
	// Math.pow(2, numberOfBits) is same as (1 << numberOfBits) this gives us a binary number whose MSB is 1 and all other bits are zeros and number of bits is 'numberOfBits + 1'   
	//If we subtract 1 from it, we get binary number of 'numberOfBits' digits and all bits are 1   
	return ((1 << numberOfBits) - 1) ^ x;
}
```

### Example: Calculate the 2’s complement of 10 in a 5 bit integer system (used for simplicity)

```
   10 : 0 1 0 1 0
=>      1 0 1 0 1 // 1's comlement
=>      0 0 0 0 1 // Adding 1
   -------------------------------
        1 0 1 1 0 // Signed presentation of -10.
```

**Note** The MSB in 2’s complement is the sign bit. It is zero for positive number and 1 for negative numbers.

## ✔️Range of datatypes

How to calculate the range of unsigned number - It is simply [0, 2^N] How to calculate the range of signed number - Calculate max - MSB = 0 // required for positive numbers - All other bits = 1 // To maximize the value represented by all other bits - Calculate min - MSB = 1 // required for negative numbers - All other bits = 1 // To minimise the value represented by all other bits - Diff

| Number of Bits | Signed | Unsigned | Range |
| --- | --- | --- | --- |
| 2 | [-2,1] | [0, 3] | 2^2 = 4 |
| 8 | [-2^7, 2^7-1] | [0, 2^8] | 2^8 = 256 |
| N | [-2^(N-1), 2^(N-1)-1] | [0, 2^N] | 2^N |

---

# ⭐ Important properties of bitwise operators

## ✔️ Basic properties of bitwise AND(&)

In this section we will discuss the properties of AND bitwise operator

### 1. Even/Odd Property

- A number is odd or even depends on Least significant bit OR LSB.
    - If LSB = 0 => Even number
    - If LSB = 1 => Odd number
- So how to check if a given binary number is even or odd.

```
Binary Number : 1 0 0 1 0 1 0 1
Bit Mask      : 0 0 0 0 0 0 0 1
------------------------------------
AND(&)        : 0 0 0 0 0 0 0 1 => This means it is odd

Binary Number : 1 0 0 1 0 1 0 0
Bit Mask      : 0 0 0 0 0 0 0 1
------------------------------------
AND(&)        : 0 0 0 0 0 0 0 0 => This means it is even
```

- Thus the alternate method of checking if a number is even or odd
    - X & 1= 1 => X is odd
    - X & 1= 2 => X is even
- So, why do we need it if we have the `%` operator
    - This is much faster because it works on bits.

### 2. A & 0 = 0

- If bitwise AND is applied with zero, result is zero.

### 3. A & A = A

- If bitwise AND is applied with itself, result is the same number.

## ✔️ Basic properties of bitwise OR(|)

### 1. A | 0 = A

- If bitwise OR is applied with zero, result is the same number.

### 2. A | A = A

- If bitwise OR is applied with itself, result is the same number.

## ✔️ Basic properties of bitwise XOR(^)

### 1. A ^ 0 = A

- If bitwise XOR is applied with zero, result is the same number.

### 1. A ^ A = 0

- If bitwise XOR is applied with itself, result is zero.

## ✔️ Commutative property

- This property tells us that the order of the operands does not matter
- Example:
    - A&B = B&A
    - A|B = B|A
    - A^B = B^A

## ✔️ Associative property

- The grouping of operators does not affect the result of the operation
- Example:
    - (A&B)&C = A&(B&C) = (A&C)&B
    - (A|B)|C = A|(B|C) = (A|C)|B
    - (AC = AC) = (AB
        
        B)
        
        (B
        
        C)
        

# ⭐ De Morgan’s law (Not applicable for bitwise operator, works only for logical operators)

De Morgan's Law is a fundamental principle in Boolean algebra that describes the relationship between the negation of a logical expression involving AND and OR operations. It consists of two laws:

1. The first law states that the negation of the conjunction (AND) of two propositions is equivalent to the disjunction (OR) of their negations. In other words, it states that "not (A and B)" is the same as "(not A) or (not B)".
2. The second law states that the negation of the disjunction (OR) of two propositions is equivalent to the conjunction (AND) of their negations. In other words, it states that "not (A or B)" is the same as "(not A) and (not B)".

```
not (A and B) = (not A) or (not B)
not (A or B) = (not A) and (not B)
```

# ⭐ Shift operations

## ✔️ Left Shift operation (<<)

**NOTE** For Simplification we will use 8 bit numbers —

- What happens on a left shift operation
    - Drop the MSB
    - Add a new Zero to LSB

Example:

```
    A : 0 0 0 0 1 0 1 0  => 10
 A<<1 : 0 0 0 1 0 1 0 0  => 20
 A<<2 : 0 0 1 0 1 0 0 0  => 40
 A<<3 : 0 1 0 1 0 0 0 0  => 80
 A<<4 : 1 0 1 0 0 0 0 0  => 160
 A<<5 : 0 1 0 0 0 0 0 0  => 64
```

- Observations
    - 1 left shift doubles the number i.e. `A<<i = A*2^i`
        - This implies `1<<i = 2^i`
        - **:boom: This can be used to create bit masks**
    - Overflow happens when the MSB that is getting dropped is 1. In an overflow, the above observation does not hold

### How to create bit masks

- If the goal is to create mask for `ith bit`, then it can be created as below

```
M = 2^i = 1<<i
```

## ✔️ Right Shift operation (>>)

- The opposite operation of left shift operation
    - Drop the LSB
    - Add a new zero to MSB

Example:

```
    A : 0 0 0 0 1 0 1 0  => 10
 A>>1 : 0 0 0 0 0 1 0 1  => 5
 A>>2 : 0 0 0 0 0 0 1 0  => 2
 A>>3 : 0 0 0 0 0 0 0 1  => 1
 A>>4 : 0 0 0 0 0 0 0 0  => 0
```

- Observations
    - Right shifting a number once is same as integer division i.e. A>>1 => A%2
    - There is no overflow/underflow in case of right shift

## ✔️ Power of left shift operation

### 1. Given a number N, set the ith bit of the number

Ans: `N | (1<<i)`

### 2. Given a number N, toggle the ith bit of the number

Ans: `N ^ (1<<i)`

### 3. Given a number N, check if the ith bit is set

Ans: `N & (1<<i)` => if the result is zero, the bit is not set, else it is set. The value where the bit is set the ans will be 2^i

### 4. Given an integer N, count the number of set bits.

```
// Approach 1
for i=1 to 32:
   Check whether the bit is set or not using N & (1<<i) and keep count
// Time complexity: O(1)

// Approach 2
count = 0
while (N > 0) {
   if (N&1 == 1) count++;
   N = N >> 1;
}
return count;
// O(log N) but max value of N is 2^31-1 which is still 31 (approx) iterations. So it is same as approach 1
```

### 5. Given an integer N, set the bits from i to j

```java
void setBits(int N, int i,  int j) {   
	for (int k=i; k<j; k++) {      
		N = N | (1<<k);   
	}
}
```

# ⭐ Problem solving using bitwise operators

### ✔️ Given an array of size N where every number occurs twice except one. Find that uniquer number

```java
int findUnique(int[] A) {   int ans = 0;   for (int x : A) ans = ans^x;   return ans;}// Time complexity: O(N)// Space complexity: O(1)
```

- How this works ?

Given array A = [2, 3, 5, 6 3, 6, 2]

```
    2  :  0 1 0
    3  :  0 1 1
    5  :  1 0 1
    6  :  1 1 0
    3  :  0 1 1
    6  :  1 1 0
    2  :  0 1 0
------------------------
XOR    :  1 0 1
```

- Observations:
    - The result of XOR is `1` when the number of set bit at the position are odd.
    - Since frequency of N-1 numbers is 2 and frequency of 1 number is unique, any bit in the XOR will be set if the bit in the unique number is set.
- Based on above approach, another approach to solve this question is

```java
void findUnique(int[] A) {   
	int ans = 0;   
	for (int i=0; i<32; i++) {      
		int count=0;      
		for (int j=0; j<N, j++) {         
			if (A[j]&(1<<i) > 0) count++;      
		}      
		if ((count&1) == 1) {         
			ans = ans | (1 << i);      
		}   
	}   
	return ans;
}

// Time complexity: O(N)
// Space complexity: O(1)
```

### ✔️ Given an integer array of size N, all numbers in the given array, occur three times except one which occurs only once, Find the unique number

- If we follow the below approach and change the second if conditions as below, we get the solution of this question.

```java
void findUnique(int[] A) {   
	int ans = 0;   
	for (int i=0; i<32; i++) {      
		int count=0;      
		for (int j=0; j<N, j++) {
         if (A[j]&(1<<i) > 0) count++;
     }
     if ((count%3) == 1) {
         ans = ans | (1 << i);
      }   
}   return ans;

}

// Time complexity: O(N)
// Space complexity: O(1)
```

### ✔️ Given an integer array of size N, all number occur twice except two numbers which occur only once. Find those two numbers

## Observations:

- If two numbers are different, their XOR cannot be zero because at least one bit will be different in the two numbers.
- This means if we take the XOR, the resultant bit at any position is `1`, this means the bit in the two unique numbers at that position were different
- So if we create 2 groups, such that
    - Do XOR of all array elements.
    - Identify the position of any set bit in the resultant XOR.
    - Divide all numbers from array into two groups such that group 1 has the identified bit is set and group 2 where identified bit is unset.
    - XOR the groups to group to identify the unique element.

```java
void findTwoUnique(int A[]) {   
	int xor = 0, setBitIndex = 0, xor1=0, xor2=0;   
	for (int x : A) xor = xor^x;   
	while (setBitIndex < 32) {      
		if ((xor & (1 << setBitIndex)) > 0) break;      
		setBitIndex++;   
	}   
	for (int x : A) {      
		if ((x & (1<<setBitIndex)) > 0) xor1 = xor1^x;      
		else xor2 = xor2^x;   
	}   
	
	return new int[] { xor1, xor2 };
}
```

### ✔️ (Maximum AND pair) Given an array of size N, find the two indices i, j such that i != j && A[i]&A[j] is maximum

```jsx
public int solve(int[] A) {
        int bitCounter = 31, ans = 0;

        while (bitCounter >= 0) {
            int count = 0;
            for (int x : A) {
                if ((x & (1<<bitCounter)) > 0) count++;
            }
            if (count >= 2) {
                ans = (ans | (1<<bitCounter));
                for (int i=0; i<A.length; i++) {
                    if ((A[i] & (1<<bitCounter)) == 0) A[i] = 0;
                }
            }
            bitCounter--;
        }

        return ans;
    }
```

### ✔️ Given an array of size N with any A[i] as either 0 or 1, find the count of subarray with bitwise OR = 1

- The idea is that in the subarray, at least one 1 should be present for the bitwise OR to become 1
- From the set theory
    - At least 1 = 1 - none (for exaple, in a school, if there are 100 students, 15 of which do not play any sport. To find how many people play at least 1 sport is 100-15)
- Using the above principle, if we find the subarrays that only have zeros.
- Solution

```jsx
public class CountOfSubArrWithORAsOne {
    public static int count(int[] A) {
        int N = A.length, total = N*(N+1)/2;

        for (int i=0; i<N; i++) {
            if (A[i] == 0) {
                int count = 0;
                //System.out.print("Index : " + i);
                while (i < N && A[i] == 0) {
                    count++;
                    i++;
                }
                //System.out.println(" Count :" + count);
                total -= (count*(count+1)/2);
            }
        }

        return total;
    }

    public static void main(String...args) {
        System.out.println(count(new int[] { 1, 0, 0, 0, 1, 1, 1, 0 }));
        System.out.println(count(new int[] { 1, 0, 1, 0, 1 }));
        
        System.out.println(count(new int[] { 0, 1, 1, 0, 0 }));
        System.out.println(count(new int[] { 0, 0, 0, 1, 1 }));
    }
}
```

# ⭐ Things to remember

| # | Description | Example/Code |
| --- | --- | --- |
| 1 | Given a number n, how to change the first unset the first set bit (from right) ? | n &= (n-1) |
| 2 | How to count the number of set bits based on above observation ? | public int numSetBits(int n) {
      int count = 0;
      while (n != 0) {
          n &= (n-1);
          count++;
      }
      return count;
} |
| 3 | How is SUM, XOR and AND related ? | A+B = A^B + (2*(A&B))

This can be validated using truth table |
| 4 | How many bits are required to represent a given number N | Ceiling of log N (base 2) |