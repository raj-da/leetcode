# [796. Rotate String](https://leetcode.com/problems/rotate-string/description/)
**Difficulty:** <span style = "Color : green">Easy</span>

## Problem Discription

Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of **shifts** on `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

* For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

 ---

### Example 1:

* **Input**: s = "abcde", goal = "cdeab"

* **Output**: true

### Example 2:

* **Input**: s = "abcde", goal = "abced"

*   **Output**: false

* **Constraints:**

    * 1 <= s.length, goal.length <= 100
    * s and goal consist of lowercase English letters.

---

## My Solution: 
1. concatinate the string: this gives you every possible shift
2. search if our goal is in that concatinated string
