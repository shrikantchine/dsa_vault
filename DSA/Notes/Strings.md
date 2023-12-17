# Strings

# What is String?

- Sequence of characters
- Order is clearly defined.
- It is represented by double quotes (")
- Can be represented in two different way - Character array - String datatype

| String | Character |
| --- | --- |
| String refers to sequence of characters represented by single data type | Character Array is a sequential collection of data type char. |
| String are immutable | Character arrays are mutable |
| Built in functions like substring(), charAt() etc can be used on Strings. | No built in functions are provided in Java for operations on Character Arrays. |
| Strings can be stored in any manner in the memory. | Elements in Character Array are stored contiguously in increasing memory locations. |
| All Strings are stored in the String Constant Pool. | All Character Arrays are stored in the Heap. |
| Not preferred for storing passwords in Java. | Preferred for storing passwords in Java. |
| A String can be converted into Character Array by using the toCharArray() method of String class. Eg: String s = “GEEKS”; char [] ch = s.toCharArray(); | A Character Array can be converted into String by passing it into a String Constructor. Eg: char[] a = {‘G’, ‘E’, ‘E’, ‘K’, ‘S’}; String A = new String(a); |
- Fundamental unit is character

# Character

A character is a 8 bits value in memory

- Capital A is represented by the value *65*
    - This mean B is represented by 66
    - C is represented by 67 and so on
- Small ‘a’ is represented by value *97*
    - This means b is represented by 98
    - c is represented by 99 and so on.
- The different between capital ‘A’ and small ‘a’ is *32* `These values are called ASCII values of the characters`

# Operations

How to represent a character:

```java
char ch = 'A'; // present the character A in memorychar ch = (char) 65; // Also represents char A in memory. This is called type casting.char ch = (char) ('a' + 1) // Represents 'b'// Below will print 97 and typecasting is not required.int x = 'a';print(x);
```

---

**NOTE** Type casting is required when converting from smaller datatype to larger datatype.

---

```java
//Q. How to convert upper case to lower case and vice versa.void toggle(char[] s) {    int n = a.length;    for (int i=0; i < n; i++) {        if (a[i] >= 65 && a[i] <= 90) print((char) (a[i] + 32));        else print((char) (a[i] - 32));    }}// Time complexity: O(n)// Space Complexity: O(1)
```

---

# Substring

- Continuous sequence of characters within a string.
- Like subarray is to array, so is substring for a given string
- A single character is also a substring,
- Entire string is also a substring.
- Formula for number of substrings in a given string `n * (n+1) / 2`

```java
/**    Given String of size N & 2 integers l, r representing the start and end of s substring.    Check whether the above mentioned substring is a palindrome.*/boolean isSubstringPalindrome(String s, int l, int r) {    while (l < r) {        if (s.charAt(l) != s.charAt(r)) return false;        l++;        r--;    }    return true;}// Time complexity: O(N)// Space complexity: O(1)
```

---

### Longest palidromic substring

```java
/**Given a string A.Find the length of longest palindromic substring of A.*/// Solution 1 - Brute forceint longestPalidrome(char[] A) {    int maxVal = 1; // Since smallest palindrome is of size 1    for (int i=0; i<A.length; i++) {        for (int j=i; j<A.length; j++) {            if (isPalidrome(A, i, j)) { // This method is defined above.                maxVal = Math.max(maxVal, j-i+1);            }        }    }    return maxVal;}//Time complexity: O(N^3)//Space Complexity: O(1)
```

### Optimization for longest palindromic substring

- For all odd length substrings
    - Consider A[i] as the center element of palindrome & expand on both sides

```java
int lengthPalindrome(char[] S) {    int maxVal = 1;    // For odd length substring    for (int i=0; i<S.length; i++) {        int left = i-1;        int right = i+1;        int currentLength = 1;        while (left >= 0 && right < S.length && S[left] == S[right]) {            currentLength += 2;            left--;            right++;        }        maxVal = Math.max(maxVal, currentLength);    }    //Even length substring    for (int i=0; i<S.length-1; i++) {        left = i;        right = i+1;        int currentLength = 0;        while (left >= 0 && right < S.length && S[left] == S[right]) {            currentLength += 2;            left--;            right++;        }        maxVal = Math.max(maxVal, currentLength);    }    return maxVal;}// Time complexity: O(N^2)// Space complexity: O(1)
```

# Why the strings are immutable ?

https://www.scaler.com/topics/why-string-is-immutable-in-java/