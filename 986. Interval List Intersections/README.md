# [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)  
**Difficulty:** <span style = "color : orange">Medium</span>

## Problem Description

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [start_i, end_i]` and `secondList[j] = [start_j, end_j]`. Each list of intervals is pairwise disjoint and in sorted order.

Return _the intersection of these two interval lists_.

A closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

The intersection of two closed intervals is a set of real numbers that are either empty or form another closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

---

### Example 1:
* **Input**: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]  
* **Output**: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]  
* **Explanation**: These are the intervals where the two lists intersect.

### Example 2:
* **Input**: firstList = [[1,3],[5,9]], secondList = []  
* **Output**: []  
* **Explanation**: One list is empty, so no intersections exist.

---

### Constraints:
* 0 <= firstList.length, secondList.length <= 1000  
* 0 <= start_i < end_i <= 10^9  
* firstList and secondList are sorted in ascending order and non-overlapping within themselves  

---
---

## Solution

We use a **two-pointer technique** to find all intersections between the two sorted interval lists.

### Key Observations:

- An intersection exists between two intervals `[a_start, a_end]` and `[b_start, b_end]` if:  
  `a_start <= b_end` and `b_start <= a_end`
- The actual intersection range is:  
  `[max(a_start, b_start), min(a_end, b_end)]`
- We need to move the pointer for the interval that ends first to continue checking possible overlaps.

### Steps:

1. Initialize two pointers `i = 0` and `j = 0`.
2. While both pointers are within bounds:
   - Extract intervals `firstList[i]` and `secondList[j]`
   - If they intersect, add `[max(start), min(end)]` to the result
   - Move the pointer whose interval ends first
3. Return the collected intersections

---

### Time and Space Complexity:

- **Time Complexity**: O(n + m) — we traverse each list once  
- **Space Complexity**: O(1) — ignoring the output list, only a few pointers/variables are used  
