# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
**Difficulty:** <span style="color: orange">Medium</span>

## Problem Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

---

### Example 1:
**Input:**  
`"abcabcbb"`  
**Output:**  
`3`  
**Explanation:** The answer is `"abc"`, with the length of 3.

### Example 2:
**Input:**  
`"bbbbb"`  
**Output:**  
`1`  
**Explanation:** The answer is `"b"`, with the length of 1.

### Example 3:
**Input:**  
`"pwwkew"`  
**Output:**  
`3`  
**Explanation:** The answer is `"wke"`, with the length of 3.  
Note that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

---

## Constraints

- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces.

---

## Solution

### Approach

We use the **sliding window** technique with a **set** to keep track of characters we've seen so far:

1. Initialize two pointers, `l` (left) and `r` (right), to represent the current window of unique characters.
2. As we iterate `r` over the string:
   - If `s[r]` is already in the set, shrink the window from the left (`l`) until `s[r]` is no longer in the set.
   - Add `s[r]` to the set and update the maximum length of substring found so far.
3. The window always contains only unique characters.

---

