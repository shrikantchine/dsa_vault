# Combinatorics

Combinatorics is the branch of mathematics which deals with Probability, Permutations and combinations.

## Agenda

1. Addition and Multiplication rule
2. Permutations Basic
3. Combinations and properties
4. Pascals Triangle
5. Nth column title

## Addition and Multiplication Rule

---

Here the idea is to understand when to add or multiple to get the answer needed.

✔️ **In a class if there are 10 girls and 7 boys. Find the total number of ways to form a couple.**

- For the first boy, all 10 girls can form couple ⇒ 10
- For the second boy, again all 10 girls can form a couple ⇒ 10
- Similarly for all boys, number of couple can be formed 10
- Thus the ans is (number of boys) * (number of girls) = 7 * 10 = 70
- There are two ways to look at this problem
- AND way

<aside>
💡 To form a couple ⇒ select a boy **AND** select a girl ⇒ Whenever there is an **AND** relation, we use multiplication

</aside>

- OR way

<aside>
💡 To form a couple ⇒ for all girls, we select Boy1 **OR** Boy2 **OR** Boy3… ⇒ 10 for Boy1 + 10 for Boy2… ⇒ Whenever there is a **OR** relation, we use addition.

</aside>

### When to use AND and Multiplication ?

If two events are given, and both are required to happen, we say, EVENT 1 AND EVENT2  both should happen. Then we multiple the possibilities of EVENT1 and EVENT2.

### When to use OR and SUM ?

If two events are given, either of the event is required to happen, then we add the possibilities of events.

---

## Permutation

---

Defined as Arrangement of objects where the order matters.

✔️ **Given 3 different characters, in how many ways, can you form a string of size 3.**

- For the first position, we have 3 possibilities.
- For the second position, we have 2 possibilities
- For the 3rd position, we have 1 possibilities
- There for the ans is 3*2*1 = 6.

<aside>
💡 For N distinct elements, the number of ways to arrange them is $N!$

</aside>

**✔️  Given N distinct characters, but only R positions where R< N. How many ways are there are to arrange the characters.**

- Arrange all elements in N positions ⇒ $N!$
- Remove the arrangements of Last R items ⇒ $(N-R)!$
- Thus the ans is:

$$
{N! \above{2pt} (N-R)!} \rArr nPr

$$

## Combinations

---

- Not concern about the order of arrangement
- It is defined as the number of ways to select something (order of selection does not matter)
- Say we have 4 players(p1, p2, p3, p4) in total and for a match, we need to select 3 players, following are the ways to select players
    - p1, p2, p3
    - p1, p2, p4
    - p1, p3, p4
    - p2, p3, p4
- To represent this, we use the symbol “C”. In this case $4C3 = 4$
- **To generalize this, to select “*r*” things from given “*n”*  things, we use $nCr$**
- So, if we select r items from n items, it gives us $nCr$. And we we want to arrange the selected items, it can be done in $R!$ ways. Thus number of ways to arrange r elements is $nCr  * R!$, which is nothing but $nPr$
- Therefore

$$
nCr = {n! \above{2pt} (n-r)! r!} 
$$

## Properties of combination

---

1. $nC0 = 1$ ⇒ The ways to select zero items from n items is 1.
2. $nCn = 1$ ⇒ The ways to select all n item from n items is 1.
3. $nCr = nC(n-r)$ ⇒ Selecting r items is same as not selecting (n-r) items.
4. Given n elements, if we want to select r element. Lets consider any random position X, we have two choices for this position
    1. We select the item at position X. Pending items are selected using: $(n-1)C(r-1)$
    2. We do not select items at position X. Pending items are selected using $(n-1)Cr$
    3. Therefore 
    
    $$
    nCr = (n-1)C(r-1) + (n-1)Cr
    $$
    
    ## Pascals Triangle
    
    ---
    
    **Problem Statement:**  
    
    Given a integer N, generate pascals triangle.
    
    **Example:** for N = 3
    
    ```
           0C0
         1C0 1C1
        2C0 2C1 2C2
       3C0 3C1 3C2 3C3
    ```
    
    **How to represent?**
    
    - Using a matrix, all values can be printed in lower half of the matrix
    - Each element of matrix is M[i][j] = $iCj$
    - Matrix will look like below for N=3
    
    ```
    i/j	 0 1 2 3
    	0  1   
    	1  1 1  
    	2  1 2 1 
    	3  1 3 3 1
    ```
    
    ```jsx
    int[][] pascalsTriangle(int N) {
    	int[][] ans = new int[N+1][N+1];
    	
    	ans[0][0] = 1;
    		for (int i=1; i<N; i++) {
    			ans[i][0] = 1;
    			ans[i][j] = 1;
    			for (int j=0; j<=i-1; j++) {
    					ans[i][j] = ans[i-1][j-1] + ans[i-1][j];
    			}
    		}
    	
    	return ans;
    }
    ```