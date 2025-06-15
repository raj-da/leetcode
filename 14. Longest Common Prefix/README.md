# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)
**Difficulty:** <span style = "Color : green">Easy</span>
## Problem Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

### Example 1:

* **Input**: strs = ["flower","flow","flight"]

* **Output**: "fl"

### Example 2:

* **Input**: strs = ["dog","racecar","car"]

* **Output**: ""
* **Explanation**: There is no common prefix among the input strings.

### Constraints:

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of lowercase English letters.

---
---

## My Solution
1. The longest our prefix sum could be is the length of the shortest string in our array.
2. For the length of our possible longest common prefix iterate over every string and collect common letters untile you enconter a difference or you finish the length.