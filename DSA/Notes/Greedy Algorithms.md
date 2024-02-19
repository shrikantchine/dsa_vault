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