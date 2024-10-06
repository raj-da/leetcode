# [1052. Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/)
**Difficulty:** <span style="color: orange">Medium</span>

## Problem Discription:
There is a bookstore owner that has a store open for `n` minutes. You are given an integer array `customers` of length `n` where `customers[i]` is the number of the customers that enter the store at the start of the `ith` minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where `grumpy[i]` is `1` if the bookstore owner is grumpy during the `ith` minute, and is `0` otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not **satisfied**. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain **not grumpy** for minutes consecutive `minutes`, but this technique can only be used **once**.

Return the **maximum** number of customers that can be satisfied throughout the day.

---

### Example 1:

* **Input**: 
    * customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

* **Output:** 
    * 16

* **Explanation:**

    * The bookstore owner keeps themselves not grumpy for the last 3 minutes.

    * The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

### Example 2:

* **Input:** 
    * customers = [1], grumpy = [0], minutes = 1

* **Output:** 
    * 1

 

### Constraints:

*   n == customers.length == grumpy.length
*   1 <= minutes <= n <= 2 * 104
*   0 <= customers[i] <= 1000
*   grumpy[i] is either 0 or 1.

---


## My Solution:
>* This problem can be solved using Fixed length sliding window technique
>1. Find the base total satisfacaction by adding customers[i] where grumpy[i] == 0
>2. Create the window and find additional customers[i] where grumpy[i] == 1
>3. While sliding the window follow the following rule:
>       * Add the new customer at the end of the window if grumpy[right] == 1
>       * Remove the customer that is left of the window if grumpy[left] == 1
>           * We only do this for grumpy[i] == 1 because grumpy[i] ==  0 is already accounted for in the base total satisfaction
> **Note:** be sure to keep the maximum additional customer when you slid the window
>4. Return total_satisfaction + max_additional_customer 