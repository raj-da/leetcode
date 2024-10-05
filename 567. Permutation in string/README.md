# [567. Permutation in string](https://leetcode.com/problems/permutation-in-string/description/)
**Difficulty:**<span style="color:orange"> Medium </span> 

## Problem Discription:  
Given two strings, **`s1`** and **`s2`**, return `true` if **`s2`** contains a **permutation** of **`s1`**, or `false` otherwise.  

In other words, return `true` if one of **`s1`**'s permutations is the substring of **`s2`**.

--- 

### Example 1:
* **Input:** 
  * s1 = "ab", s2 = "eidbaooo"  
* **Output:**
  * true  
* **Explanation:**
  * s2 contains one permutation of s1 ("ba").  

### Example 2:  
* **Input:** 
  *s1 = "ab", s2 = "eidboaoo"
* **Output:** 
  *false

---
## My Solution:  
* The problem can be solved using a **fixed-size sliding window** approach:
  1. Count the letters in `s1` and store them in a dictionary.
  2. Create a window of the same size as `s1` on `s2` and count the letters in that window, storing them in another dictionary.
  3. Compare the two dictionaries. If they are equal, return `true`. If not, shift the window and continue.