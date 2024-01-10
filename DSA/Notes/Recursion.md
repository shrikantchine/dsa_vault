# Recursion

##  Tower of Hanoi

![Untitled](tower_of_hanoi.png)

**Problem statement:** 

There are 3 towers - A, B and C. A is source tower and C is destination tower.

There are N disks of different sizes present on the source tower (A). arranged like smaller on top of bigger.

Print the movement in disks from A to C in minimum number of steps.

**Conditions:**

1. Only 1 disks can be moved in a step
2. Larger disk cannot be placed on top of smaller disk.

💡 **************Solution**************

1. If N = 1, the steps required are 1 (A → C)
2. If N = 2, the steps are 3 (A → B, A → C, B → C)
3. If N=3,
    1. We need to move the top 2 towers to tower B OR use the solution of N=2 but destination is B instead of C.
    2. Move the largest disk from A to C.
    3. Move the 2 disks from tower B to tower C using solution from N=2. Here the source is B and target is C.
    4. Thus the ans is 3+1+3 = 7
4. If N=4
    1. We need to move the top 3 towers to tower B OR use the solution of N=3 but destination is B instead of C.
    2. Move the largest disk from A to C.
    3. Move the 3 disks from tower B to tower C using solution from N=3. Here the source is B and target is C.
    4. Thus the ans is 7+1+7 = 15

Thus - Total number of steps are required = 2^N - 1

```java
static void TOH(int N, String src, String dest, String intermediate) {
   if (N == 0) {
      return;
   }
   TOH(N-1, src, intermediate, dest);
   System.out.print(N + " disk moves from " + src + " => " + dest + "; ");
   TOH(N-1, intermediate, dest, src);
}

// TC : O(2^N)
// SC : O(N) => Max number of recursive call is N+1
```

##  Valid Parenthesis

**************************************Problem statement:************************************** 

For any given integer N, print valid parenthesis of length 2N 

Conditions:

1. Number of closing brackets should be equals to opening brackets
2. Each closing bracket must close an opening bracket

💡 ************Backtracking************ 

DO STEP: Make a recursive call to a sub problem

SOLVE STEP: Solve the sub problem

UNDO STEP: Undo the changes made for current sub problem

**💡 Pruning**

Stopping recursion if it leads to invalid result

```java
void validParenthesis(int N) {
	generate(N, 0, 0, "");
}

void helper(int N, int countOpen, int countClose, String curr) {
	if (curr.length() == 2*N) {
		System.out.println(curr);
		return;
	}
	if (countOpen < N) {
		generate(N, countOpen+1, countClose, curr + "(");
	}
	if (countClose < countOpen) {
		generate(N, countOpen, countClose+1, str+")");
	}
}
```

/TODO . Reduce the space using char array of size 2N

## Backtracking
