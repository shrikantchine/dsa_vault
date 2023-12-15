# Interview Questions

### ⭐ Merge intervals

- ✔️ What is an interval ?
    - Interval defined by `[start_time, time]` OR `[s, e]`
    - For solving problems, intervals will be integer starting at 0 ending at given value.
- ✔️ What does it mean to merge interval?
    - I1 = (s1, e1)
    - I2 = (s2, e2)
    - Given s2 < e1 AND e2 > e1
    - Ans: (s1, e2)
- ✔️ When can we merge two given interval ?
    - They must overalap.
    - Example:
        - I1 = (s1, e1)
        - I2 = (s2, e2)
        - Conditions where merge is not possible => s2 > e1 AND s1 > e2 (It is important to check both possibilities)
- ✔️ Example of merge intervals

```
Timeline :   1, 2, 3, 4, 5, 6, 7, 8
Inteval 1:      *************          (2, 6)
Inteval 1:         *************       (3, 7)
---------------------------------------------
After merge:    ****************       (2, 7)
```

- ✔️ Code sample to check overlap

```java
if (s2 > e1 || s1 > e2) {    // NO overlap} else {    // Overlap}
```

- ✔️ How to find the merge interval ?
    - Merged start = min(s1, s2)
    - Merged end = max(e1, e2)
- ✔️ Given a sorted list of overalapping intervals, sorted on the basis of start time, merge all overalapping intervals and return a final sorted list.
- Example:

```
s : [0, 1, 5, 6,  7, 8, 12]
e : [2, 4, 6, 8, 10, 9, 14]

ANS => s : [0,  5, 12]
       e : [4, 10, 14]
```

- Solution:
    - Start with I1 = Interval 1.
    - mark it as most recent interval (MRI)
    - For other intervals, `I`:
        - if the interval is overalapping => (e1 >= s2) i.e. intervals are already sorted:
            - MRI[start] = min(I[start], MRI[start])
            - MRI[end] = max(I[end], MRI[end])
            - Update MRI in Ans List else:
            - Move MRI to Ans List
            - MRI = I
- Code:

```java
// Matrix based approachList<List<Integer>> merge(int[][] intervals) {    int[] MRI = intervals[0];    List<List<Integer>> ans = new ArrayList<>();    for (int i=1; i<intervals.length; i++) {        int s1 = MRI[0];        int e1 = MRI[1];        int s2 = intervals[i][0];        int e2 = intervals[i][1];        if (e1 >= s2) { //Overlapping            MRI[0] = Math.min(s1, s2);            MRI[1] = Math.max(e1, e2);        } else {            ans.add(Arrays.asList(MRI));            MRI = intervals[i];        }    }    ans.add(Arrays.asList(MRI));    return ans;}// Object based approachclass Interval {    int start, end;    Interval(int start, int end) {        this.start = start;        this.end = end;    }}List<Interval> merge(int[][] intervals) {    List<Inteval> ans = new ArrayList<>();    int currS = A[0].start;    int currE = A[0].end;    for (int i=1; i < N; i++) {        if (A[i].start <= currE) {            currS = Math.min(currS, A[i].start); // Not required because of sorted            currE = Math.max(currE, A[i].end);        } else {            Interval tmp = new Interval(currS, currE);            ans.add(tmp);            currS = A[i].start;            currE = A[i].end;        }    }    Interval tmp = new Interval(currS, currE);    ans.add(tmp);    return ans;}// Time complexity: O(N)// Space complexity: O(1)
```

- ✔️ Given a sorted list of non overalapping intervals, sorted on the start time. Insert a new given interval such that final list of intervals is also sorted and non overalapping.
- Example:

```
Given Array A as below:
    s : [1, 4, 10, 16, 21, 27, 32, 28, 43]
    e : [3, 7, 14, 19, 24, 30, 35, 41, 50]

New given interval: (12, 22)

ANS: Since it merges with 3 given intervals, we merge those three and the new interval, thus the ans is

    s : [1, 4, 10, 27, 32, 28, 43]
    e : [3, 7, 24, 30, 35, 41, 50]
```

- Observations:
    - The given new interval may not be overlapping
    - The given new interval may merge with the last element // Edge case for last print statement in the below code
    - The given new interval may not be overlapping but is also the last element i.e. bigger than all elements // Edge case of last print statement in the below code.
    - Once the merge for overlap is complete, the rest of the elements in the given array can be printed as are. // Reason for return in the below code.

```java
void merge(List<Interval> intervals, int newStart, int newEnd) {
    for(int i=0; i<intervals.size(); i++) {
        int L = interval[i].start;
        int R = interval[i].end;
        if (newStart > R) {
            // No overlap
            System.out.println(L + " " + R);
        } else if (L > newEnd) {
            // No overalap but [L, R] comes after [newStart, newEnd]
            System.out.println(newStart + " " + newEnd);
            for (int j=i; j<intervals.size(); j++) {
                System.out.println(interval[j].start + " " + interval[i].end);
            }
            return;
        } else {
            newStart = Math.min(L, newStart);
            newEnd = Math.max(R, newEnd);
        }
    }
    System.out.println(newStart + " " + newEnd);
}

// Time complexity: O(N)
// Space complexity: O(1)
```

- ✔️ Given an unsorted array of integers, find the first missing natural number
- Brute force: Check if all natural numbers starting from 1 are present in the array

```java
int solve(int[] A) {
    int i=1;
    while (true) {
        boolean isFound = false;
        for (int j=0; j<N; j++) {
            if (A[j] == i) {
                isFound = true;
                break;
            }
        }
        if (!isFound) return i;
    }
}
// Time complexity: O(N^2)
// Space complexity: O(1)
```

- Observations:
    - for input size is N, the max number that is missing is N+1
    - To optimize the inner loop in the brute force solution, we can use a HashSet. This increases time complexity to O(N)
    - Sorting will reduce the space complexity O(1) but increases the time complexity to O(NlogN)