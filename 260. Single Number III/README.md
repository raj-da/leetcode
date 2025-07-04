# [260. Single Number III](https://leetcode.com/problems/single-number-iii/)
**Difficulty:** <span style="color: orange">Medium</span>

## Problem Description

Given an integer array `nums`, in which **exactly two elements appear only once** and all the other elements appear **exactly twice**, return *the two elements that appear only once*. You can return the answer in **any order**.

---

### Example 1:

**Input:**  
`nums = [1,2,1,3,2,5]`  
**Output:**  
`[3,5]`  
**Explanation:**  
The numbers `3` and `5` appear only once; all others appear twice.

---

### Example 2:

**Input:**  
`nums = [-1,0]`  
**Output:**  
`[-1,0]`

---

### Example 3:

**Input:**  
`nums = [0,1]`  
**Output:**  
`[1,0]`

---

### Constraints:

- `2 <= nums.length <= 3 * 10^4`
- Each integer in `nums` appears exactly twice, except for two elements that appear only once.
- The solution must run in linear time and use constant extra space.

---

## My Solution:

1. XOR all numbers to get `xor_result = a ^ b` (where `a` and `b` are the unique numbers).
2. Find any set bit in `xor_result`. This bit **must differ between `a` and `b`**.
3. Split the array into two groups using this bit:
   - One group with the bit set
   - One group with the bit not set
4. XOR within each group to isolate `a` and `b`.

---