# [2024. Maximizing the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/)
**Difficulty:** <span style = "color: orange">Medium</span>  

## Problem Discription:  
A teacher is writing a test with `n` true/false questions, with `'T'` denoting true and `'F'` denoting false. He wants to confuse the students by **maximizing** the number of **consecutive** questions with the **same** answer (multiple trues or multiple falses in a row).  

You are given a string `answerKey`, where `answerKey[i]` is the original answer to the `ith` question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:  

* Change the answer key for any question to `'T'` or `'F'` (i.e., set `answerKey[i]` to `'T'` or `'F'`).  

Return the **maximum number of consecutive `'T'`s or `'F'`s in the answer key after performing the operation at most `k` times.  

---
### Example 1:
* **Input:**
  * answerKey = "TTFF", k = 2
* **Output:**
  * 4
* **Explanation:**
  * We can replace both the 'F's with 'T's to make answerKey = "TTTT".
  * There are four consecutive 'T's.

### Example 2:  
* **Input:**
  * answerKey = "TFFT", k = 1
* **Output:**
  * 3
* **Explanation:**
  * We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
  * Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
  * In both cases, there are three consecutive 'F's.

### Example 3:
* **Input:**
  * answerKey = "TTFTTFTT", k = 1
* **Output:**
  * 5
* **Explanation:**
  * We can replace the first 'F' to make answerKey = "TTTTTFTT"
  * Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
  * In both cases, there are five consecutive 'T's.

---
## My Solution:
>* This problem can be solved using variable length sliding window technique
>1. **Track the frequency of** `T` and `F` in your current sliding window using a dictionary (or a similar data structure).
>2. Keep track of the **maximum frequency** between `T` and `F` in the window. This helps determine if the window is valid.
>3. **A valid window** is one where:  
>            (**_length of the window_ - _maximum frequency_ ≤ k**)  
>   This means you can flip k or fewer characters to make all characters in the window the same.
>4. **Important Note:** You only need to update the maximum frequency when you find a higher value. Once you have the highest frequency in a window, even if you shrink the window later, you don’t need to adjust the maximum frequency. This is because the best solution (longest valid window) is always found when the frequency was at its highest.
>5. As you slide the window, keep track of the lengths of valid windows and return the **maximum length**.