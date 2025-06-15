# [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/description/)  
**Difficulty:** <span style="color: orange">Medium</span>

## Problem Description

Given an array of positive integers `nums` and an integer `k`, return _the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than_ `k`.

---

### Example 1:

* **Input**: nums = [10, 5, 2, 6], k = 100  
* **Output**: 8  
* **Explanation**: The 8 subarrays that have product less than 100 are:  
  [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

### Example 2:

* **Input**: nums = [1, 2, 3], k = 0  
* **Output**: 0

---

### Constraints:

* `1 <= nums.length <= 3 * 10^4`
* `1 <= nums[i] <= 1000`
* `0 <= k <= 10^6`

---
---

## My Solution
1. A variable size sliding window
2. keep track of product in the window and count number of subarrays in the window using r - l + 1
3. shrink the window if product exceeds k