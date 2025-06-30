# [594. Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence)
###  Medium

---

### Problem Description

We define a harmonious array as an array where the **difference between its maximum value and its minimum value is exactly 1**.

Given an integer array `nums`, return *the length of its longest harmonious subsequence* among all its possible subsequences.

---

### Example

**Input:**
nums = [1,3,2,2,5,2,3,7]


**Output:**

**Explanation:**  
The longest harmonious subsequence is `[3,2,2,2,3]`.  
It contains both 2 and 3, and their count adds up to 5.

---

### Constraints
- `1 <= nums.length <= 2 * 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`

---

##  Solution

1. Count the frequency of each number in the array using `Counter`.
2. For each number `num` in the frequency map:
   - Check if `num - 1` exists in the frequency map.
   - If it does, it forms a harmonious subsequence with `num`, and we compute the total count as `frequency[num] + frequency[num - 1]`.
   - Keep track of the maximum such count seen so far.
3. Return the maximum count.

---