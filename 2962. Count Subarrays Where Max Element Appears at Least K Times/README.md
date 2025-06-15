# [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)  
**Difficulty:** <span style = "color : orange">Medium</span>

## Problem Description

You are given an integer array `nums` and a positive integer `k`.

Return _the number of subarrays where the maximum element appears at least_ `k` _times_.

---

### Example 1:
* **Input**: nums = [1,3,2,3,3], k = 2  
* **Output**: 6  
* **Explanation**: The subarrays where the maximum element (3) appears at least 2 times are:
  - [1,3,2,3]
  - [1,3,2,3,3]
  - [3,2,3]
  - [3,2,3,3]
  - [2,3,3]
  - [3,3]

### Example 2:
* **Input**: nums = [1,4,2,1], k = 3  
* **Output**: 0  
* **Explanation**: The maximum element is 4 and it never appears at least 3 times in any subarray.

---

### Constraints:
* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`
* `1 <= k <= nums.length`

---
---

## Solution

We use a **sliding window** technique to count the number of valid subarrays where the **maximum element appears at least `k` times**.

### Key Observations:

- Let `maxVal` be the maximum element in the entire array.
- Only subarrays that include `maxVal` at least `k` times are valid.
- We will count all such subarrays efficiently using two pointers.

### Steps:

1. **Track the count of `maxVal`** in the current window `[l, r]`.
2. Expand the right pointer `r` in the loop.
3. When the count of `maxVal` in the window becomes at least `k`, then:
   - All subarrays starting from `l` to the end of array (`n - r`) are valid.
   - We then try to move the left pointer `l` forward to find the next minimal valid window.
4. Keep adding the number of valid subarrays found to a result counter.

### Why Count `(n - r)`?

For any valid window `[l, r]` with `k` or more occurrences of `maxVal`, any extension of this window to the right will still satisfy the condition. So we can count all subarrays starting at `l` and ending at `r`, `r+1`, ..., `n-1` → that’s `n - r` subarrays.

---

### Time and Space Complexity:

- **Time Complexity**: `O(n)` — each element is processed at most twice (once by each pointer).
- **Space Complexity**: `O(1)` — we use only a few variables for tracking.

