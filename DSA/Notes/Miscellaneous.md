
### Perfect numbers

**Problem statement**
Given an integer A, find the Ath perfect number. 

Perfect number:
- Comprises of 1 and 2
- The number of digits are even
- It is a palindrome

**Example**

| Number | is Perfect number ? |
| ------ | ------------------- |
| 11     | yes                 |
| 111    | no                  |
| 12     | no                  |
| 22     | yes                 |
| 123    | no                  |
| 1111   | yes                 |
| 112211 | yes                 |
| 2212   | no                  |
**Solution**

- Perfect number series
```
11, 22, 1111, 1221, 2112 ...
```

- Since all these numbers are palindrome, lets look at the first half and build the series
```
1, 2, 11, 12, 21, 22 ...
```

- So, the approach could be
	- Use a queue data structure
	- Insert 1 and 2 in the queue.
	- Remove the front of the queue.
	- Append 1 to it for the next number, insert it into the queue.
	- Append 2 to it for the next number, insert it into the queue.

```java
String perfectNumber(int A) {
	if (A == 1) return "11";
	if (A == 2) return "22";
	
	Deque<String> queue = new LinkedList<>();
	queue.addLast("1");
	queue.addLast("2");
	StringBuilder answer = new StringBuilder();
	int count = 3;

	if (count <= A) {
		StringBuilder sb = new StringBuilder(queue.poll());
		if (count == A) {
			answer = sb;
			break;
		}
		sb.append("1");
		queue.add(sb.toString());
		sb.deleteCharAt(sb.length()-1);
		sb.append("2");
		queue.add(sb.tostring());
		count++;
	}

	return ans.toString() + sb.reverse().toString();
}
```

### Copy of a linked list

**Problem Statement**

Given a linked list, return a deep copy of it.