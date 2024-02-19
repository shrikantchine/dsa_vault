## Introduction



## Questions
### Profit vs Expiry

**Problem Statement**

A grocery store wants to promote its products to ensure maximum profit. For this we are given an array A of expiry dates of each item and array B contains the profit of each item.
Design an algorithm to maximise the profit.

Example: 
```
A = [3, 1, 3, 2, 3]
B = [6, 5, 3, 1, 9]

Answer = 20 (At T=3, all products will expire)
```

Constraints:
1. It takes 1 unit of time to sell 1 product. 
2. Timer starts from T=0
3. Only sell a product before T < A[i] i.e. before expiry

**Solution**
1. If we just select *profit* as the criterion for selection of a product, the max profit that we can achieve is `18`. Thus we need to amend the criterion.
2. Solution:
	1. Sort the expiry time array and sort the profit array according to expiry array.
	2. Loop through the expiry array A, 
	3. Run a counter T to measure time units which is incremented at each loop iteration
	4. At some T, if the item at `i` can be sold, make a choice to sell it.
	5. Otherwise, look back to check a better solution => Find the item with min profit, make a choice to not sell it and sell the item at `i` if it gives more profit. Do not increment the counter `T` here.

```java
int maximiseProfit(int[] A, int[] B) {
	// SORT
	Item[] items = new Items[A.length];
	for (int i=0; i<A.length; i++) {
		items.add(new Item(A[i], B[i]));
	}
	Arrays.sort(items, (i1, i2) -> Integer.compare(i1.expiry, i2.profit)); 

	// Main Logic
	PriorityQueue<Integer> heap = new PriorityQueue<>();
	int counter = 0, result = 0;

	for (int i=0; i<items.length; i++) {
		if (items[i].expiry > counter) {
			result += items[i].profit;
			heap.add(items[i].profit);
			count++;
		} else {
			int minProfit = heap.poll();
			if (minProfit < items[i].profit]) {
				result -= minProfit;
				result += items[i].profit;
				heap.add(items[i].profit);
			}
		}
	}

	return result;
}

class Item {
	int expiry;
	int profit;

	Item(int expiry, int profit) {
		this.expiry = expiry;
		this.profit = profit;
	}
}
```

**Complexity Analysis**

Time Complexity: O(n log n) => Because of sorting
Space complexity: O(n)

### Minimum Candies required

**Problem Statement**
There are N students in a class. After their exam results, teacher wants to distribute candies to them as per below constraints

1. Every student must have at least 1 candy.
2. Student with marks more than his/her neighbour should be given more candies compared to neighbours.

Find the minimum number of candies required.

Example:

```
Example 1:

	A        = [1, 5, 2, 1, 10]
	Candies  = [1, 3, 2, 1, 2]
	Total candies = 9

Example 2:
	A        = [4, 4, 4, 4, 4]
	Candies  = [1, 1, 1, 1, 1]
	Total candies = 5
```

**Solution**

- Since the problem here is that we need to know the number of candies given to both left and right neighbour before deciding the number of candies for current student, it is not possible to do this with 1 iteration (from left to right or right to left).
- So, we will use 2 array

```text
A                  = [1, 6, 3, 1, 10, 12, 20, 5, 2]
Candies from Left  = [1, 2, 1, 1, 2,  3,  4,  1, 1] => This is being greedy
Candies from right = [1, 3, 2, 1, 1,  1,  3,  2, 1] => This is being greedy
Ans                = [1, 3, 2, 1, 2,  3,  4,  2, 1] => Max of left and right
```

```java
int maxCandies(int[] A) {
	int n = A.length, ans = 0;
	int[] cl = new int[n];
	int[] cr = new int[n]
	cl[0] = 1;
	for (int i=1; i<n; i++) {
		if (A[i] > A[i-1]) {
			cl[i] = cl[i-1] + 1;
		} else {
			cl[i] = 1;
		}
	}

	cr[n-1] = 1;
	for (int i=n-2; i>=0; i--) {
		if (A[i] > A[i+1]) {
			cr[i] = cr[i+1]+1;
		} else {
			cr[i] = 1;
		}
	}

	for (int i=0; i<n; i++) {
		ans += Math.max(cl[i], cr[i]);
	}

	return ans;
}
```

**Complexity Analysis**

Time Complexity: O(n)
Space complexity: O(n)

### Maximum Jobs

**Problem statement**

Given N jobs defined by `[start_time, end_time]` . Find max number of jobs that can be completed if only 1 job can be done at a time.

**Solution**

- To maximise the number of jobs taken, sort based on `end time`
- Iterate and check if job at current index `i` can be completed. A job can be completed if its start time is greater than or equal to end time of previous job.

```java
class Job {
	int start;
	int end;

	Job(int start, int end) {
		this.start = start;
		this.end = end;
	}
}

int countJobs(Job[] jobs) {
	Arrays.sort(jobs, (j1, j2) -> Integer.compare(j1.end, j2.end));
	int count = 1;
	int lastEndTime = jobs[0].end;

	for (int i=1; i<jobs.length; i++) {
		if (jobs[i].start >= lastEndTime) {
			count++;
			lastEndTime = jobs[i].end;
		}
	}

	return count;
}
```

**Complexity Analysis**

Time Complexity: O(n log n) =>  because of sorting
Space complexity: O(n)