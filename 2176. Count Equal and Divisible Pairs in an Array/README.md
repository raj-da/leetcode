# [2176. Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/)
**Difficulty:** <span style="color: green">Easy</span>

## Problem Description

You are given a **0-indexed** integer array `nums` and an integer `k`.

A pair of indices `(i, j)` is called **good** if:
- `i < j`
- `nums[i] == nums[j]`
- `(i * j) % k == 0`

Return the number of **good pairs**.

---

### Example 1:

**Input:**  
`nums = [3,1,2,2,2,1,3]`, `k = 2`  
**Output:**  
`4`

**Explanation:**  
There are 4 good pairs:  
- (0, 6), (1, 5), (2, 3), (2, 4)

---

### Example 2:

**Input:**  
`nums = [1,2,3,4]`, `k = 1`  
**Output:**  
`0`

---

### Constraints:

- `1 <= nums.length <= 100`
- `1 <= nums[i], k <= 100`

---

## My Solution:

1. Use a dictionary to map each value in `nums` to a list of indices where that value appears.
2. For each value, compare the current index with all previous indices where the same value occurred.
3. Check whether the product of indices is divisible by `k`.
4. Count how many such valid pairs exist.
