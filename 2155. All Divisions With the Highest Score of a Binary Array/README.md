# [2155. All Divisions With the Highest Score of a Binary Array](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/)
**Difficulty:** <span style="color: green">Easy</span>

## Problem Description

You are given a **0-indexed binary array** `nums` (i.e., it only contains `0` and `1`).

We can split `nums` at any index `i` (where `0 <= i <= nums.length`) into two parts:
- `left = nums[0..i - 1]`
- `right = nums[i..n - 1]`

The **score of a split** is the number of `0`s in the left part + the number of `1`s in the right part.

Return *every index `i` where the score is maximized*. The answer can be returned in any order.

---

### Example 1:

**Input:**  
`nums = [0,0,1,0]`

**Output:**  
`[2,4]`

**Explanation:**  
- Score at index 0 = 0 + 2 = 2  
- Score at index 1 = 1 + 2 = 3  
- Score at index 2 = 2 + 1 = 3 ← ✅  
- Score at index 3 = 2 + 0 = 2  
- Score at index 4 = 3 + 0 = 3 ← ✅  

So, indices `[2, 4]` give the maximum score of 3.

---

### Example 2:

**Input:**  
`nums = [0,0,0]`

**Output:**  
`[3]`

**Explanation:**  
All 0s → only best score is when all are on the left: 3 zeros + 0 ones = 3

---

### Constraints:

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

---

## My Solution:

1. Compute a prefix sum of the number of `1`s up to each index.
2. For every possible split index `i` (from `0` to `len(nums)`), calculate:
   - Number of `0`s in the left part = `i - prefix_ones[i]`
   - Number of `1`s in the right part = `total_ones - prefix_ones[i]`
3. Track the max score and collect all indices where the score equals the max.

---