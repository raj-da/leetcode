# [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)
**Difficulty:** <span style = "Color : orange">Medium</span>
## Problem Discription
A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `ith` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

---

### Example 1:

* **Input**:weights = [1,2,3,4,5,6,7,8,9,10], days = 5

* **Output**: 15
* **Explanation**:A ship capacity of 15 is the minimum to ship all the packages in 5 days like this: <br>
1st day: 1, 2, 3, 4, 5 <br>
2nd day: 6, 7 <br>
3rd day: 8 <br>
4th day: 9 <br>
5th day: 10 <br>

### Example 2:

* **Input**: s = "abcde", goal = "abced"

*   **Output**: false

* **Constraints:**

    * 1 <= s.length, goal.length <= 100
    * s and goal consist of lowercase English letters.

---