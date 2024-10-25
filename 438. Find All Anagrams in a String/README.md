# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)
**Difficulty:** <span style = "Color : orange">Medium</span>

## Problem Discription

Given two strings `s` and `p`, return an array of all the start indices of `p`'s 
**anagrams**
 in `s`. You may return the answer in **any order**.

 ---

### Example 1:

* **Input**: 
    * s = "cbaebabacd", p = "abc"
* **Output**: 
    * [0,6]
* **Explanation**:
    * The substring with start index = 0 is "cba", which is an anagram of "abc".
    * The substring with start index = 6 is "bac", which is an anagram of "abc".

### Example 2:

* **Input**: 
    * s = "abab", p = "ab"
*   **Output**:
    * [0,1,2]
* **Explanation:**
    * The substring with start index = 0 is "ab", which is an anagram of "ab".
    * The substring with start index = 1 is "ba", which is an anagram of "ab".
    * The substring with start index = 2 is "ab", which is an anagram of "ab".
 

* **Constraints:**

    * 1 <= s.length, p.length <= 3 * 104
    * s and p consist of lowercase English letters.

---

## My Solution: 
* This problem can be solved using fixed size sliding window
    1. The size of the sliding window will be the length of `p`
    2. For `every window` compare the number of characters to that of the number of characters in `p`
        * If the same add the left most index of the window to you solution
        * If not shrink the window
