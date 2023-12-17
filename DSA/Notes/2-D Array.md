# 2-D Array

### 💡 Given a 2D array of size NxM, where the elements are sorted in each row and each column, search an element K.

### Brute force:

- Iterate over all elements and seach the element
- TC: O(N*M)
- SC: O(1)

### Optimized solution

- Start at first row and last colum
    - Can also start at first column and last row
    - Why ? because from this posistion if we go down, the value increases and if we go left, the value decreases.
- If the value at current index is equal to target, return `true`
- if value at current index is less than target, decrease the column (because since it is sorted, values that come before in the current row, are less than current value)
- Similarly if the current index is greater than target, increase the row.

```java
boolean search(int A[][], int target, int N, int M) {
    int i = 0, j = M-1;
    while (i < N && j >=0) {
        if (A[i][j] == target) return true;
        if (A[i][j] < target) j--;        
				else i++;
    }    
		return false;
}
```

### 💡 Given a binary matrix M i.e. any value M[i][j] is either 0 or 1. The matrix is row wise sorted. Find the row with max number of 1s. In case of multiple rows with same number of 1s, return the one with lower index.

### Brute force:

- Iterate over all rows, count number of 1s
- Compare the counts and get max.
- TC: O(N*M)
- SC: O(1)

### Optimal solution

- Observation: If we iterate over the first array and see if the last two elements are 1s. This means that we never have to check any element of last two columns.
- So, the solution should be
    - Start at [0, M-1]
    - Loop till you exit the matrix
    - if you find 1, go left
    - On the last 1, go down to find a better count of 1.
    - if we find a 0, ignore the row since we have already found a row with more 1s at previous index.
- TC: O(N+M)
- SC: O(1)

```java
void findMaxOnesRow(int[][] A, int N, int M) {
    int i=0, j=M-1, index=0;
    while (i < N && j >= 0) {
        if (A[i][j] == 1) {
            j--;
            index = i;
        } else {
            i++;
        }
    }
    return index;
}
```

### 💡 Given a matrix of size NxN, print the boundary elements in a clock-wise direction starting from the cell (0, 0)

```
Exmple:
    A[][] = [ [1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
            ]
    Ans: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]
```

- Observation: It will be easier to implement this in 4 different loop
- It would be easier to print `N-1` elements in each loop.
- Steps
    1. Print N-1 elements in the first row from left to right
    2. Print N-1 elements in last colum from top to bottom starting at top.
    3. Print N-1 elements in last row from right to left
    4. print N-1 elements in 1st column from bottom to top.

```java
void printBoundaries(int A[][], int N) {
    int i=0, j=0;
    for (int count=0; count<N-1; count++) {
        System.out.println(A[i][j]);
        j++;
    }
    for (int count=0; count<N-1; count++) {
        System.out.println(A[i][j]);
        i++;
    }
    for (int count=0; count<N-1; count++) {
        System.out.println(A[i][j]);
        j--;
    }
    for (int count=0; count<N-1; count++) {
        System.out.println(A[i][j]);
        i--;
    }
}

// Time complexity: O(N)
// Space complexity: O(1)
```

### 💡 Spiral order matrix => Print the matrix of size N, print in spiral form.

```
Exmple:
    A[][] = [ [1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16],
            ]
    Ans: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
```

Observation: - After printing 1 boundary, we need to print the boundary of inner matrix. - Number of columns in inner matrix = number of columns in outer mtrix + 2 - After the first outer loop, i and j will reach 0 and 0 again. So going to inner loop is moving through diagonal i.e. i+1 and j+1 - Edge case: If we reach 1*1 matrix, just print it. So we only need 4 loops till N>=2

```java
void printSpiral(int A[][], int N) {
    int i=0, j=0, k=N;
    while (k >= 2) {
        for (int count=0; count<k-1; count++) {
            System.out.println(A[i][j]);
            j++;
        }
        for (int count=0; count<k-1; count++) {
            System.out.println(A[i][j]);
            i++;
        }
        for (int count=0; count<k-1; count++) {
            System.out.println(A[i][j]);
            j--;
        }
        for (int count=0; count<k-1; count++) {
            System.out.println(A[i][j]);
            i--;
        }
        i++;
        j++;
        k-=2;
    }
    if (k == 1) {
        System.out.println(A[i][j]);
    }
}

// Time complexity: O(N^2)
// Space complexity: O(1)
```

# ⭐ Sub-Matrix

### What is subarry ?

Continuous part of array from any element `s` to the element `e` presenting the start and end indices of subarary

### ✔️ What is sub-matrix ?

Continuous smaller matrix inside a bigger matrix.

- What do I need to define it ?
    - Start column (c1)
    - End column (c2)
    - Start row (r1)
    - End row (r2)
- How many elements are required.
    - Every points where r1, r3, c1, c2 are intesecting
    - So below are the combinations
        - (r1, c1) OR (r2, c1) => Starting cell of the submatrix
        - (r2, c2) OR (r1, c2) => Ending cell of the submatrix
- One cell can also be a submatrix of size 1*1

### 💡 Given a matrix of size NxM. Print a given submatrix from (r1, c1) and (r2, c2)

```java
void print(int[][] A, int r1, int r2,  int c1, int c2) {
    for (int i=r1;i <= r2; i++) {
        for (int j=c1; j<=c2; i++) {
            System.out.println(A[i][j]);
        }
    }
}
```

### 💡 Given a matrix of size NxM. Find the sum of a given submatrix from (r1, c1) and (r2, c2)

```java
int print(int[][] A, int r1, int r2,  int c1, int c2) {
    int sum = 0;
    for (int i=r1;i <= r2; i++) {
        for (int j=c1; j<=c2; i++) {
            sum += A[i][j];
        }
    }
    return sum;
}
```

### 💡 Sum of all submatrices

- How to extend the `contribution technique` for a matrix
- Lets divide the problems in parts as below
    - How to find all submatrices ?
    - Find the sum of the sub matrix

### How to find all submatrices ?

- Starting row of submatrix cannot be greater than ending row => r1 <= r2
- Starting column of submatrix cannot be greater than ending column => c1 <= c2

```java
void solve(int[][] A, int N, int M) {
    for (int r1=0; i< N; r1++) {
        for (int c1=0; i<M; c1++) {
            for (int r2=r1; r2 < N; r2++) {
                for (int c2=c1; c2<M; c2++) {
                }
            }
        }
    }
}

// Time complexity: O(N^2 * M^2)
```

### Find the sum of sub matrix

```java
void solve(int[][] A, int N, int M) {
    int sum = 0;
    for (int r1=0; i< N; r1++) {
        for (int c1=0; i<M; c1++) {
            for (int r2=r1; r2 < N; r2++) {
                for (int c2=c1; c2<M; c2++) {
                    int sum = 0;
                    for (int i=r1;i <= r2; i++) {
                        for (int j=c1; j<=c2; i++) {
                            sum += A[i][j];
                        }
                    }
                    ans += sum;
                }
            }
        }
    }
    return ans;
}

// Time complexity: O(N^3 * M^3)
```

### Using contribution technique

- Contribution of `M[i][j]` element towards the total = (Number of submatrices where A[i][j] is present) * (M[i][j])

Observations: - r1 : [0, i] => i+1 // total - r2 : [i, N-1] => N-i // total - c1 : [0, j] => j+1 // total - c2 : [j, M-1] => M-j // total ——————————– Multiply these values to get total number of subarrays where element A[i][j] is present

```
(i+1) * (N-i) * (j+1) * (M-j)
```

How to code:

```java
void findTotalSubMatrixSum(int A[][], int N, int M) {
   int ans = 0;
   for (int i=0; i<N; i++) {
       for (int j=0; j<M; j++) {
           int count = (i+1) * (N-i) * (j+1) * (M-j);
           int contribution = count * A[i][j];
           ans += contribution;
       }
   }
   return ans;
}

// Time complexity: O(N*M)
// Space complexity: O(1)
```