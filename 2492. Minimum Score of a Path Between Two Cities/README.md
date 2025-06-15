# [2492. Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)  
**Difficulty:** <span style = "color : orange">Medium</span>

## Problem Description

You are given a positive integer `n`, representing the number of cities from `1` to `n`.  
You are also given a 2D array `roads`, where `roads[i] = [ai, bi, distance_i]` denotes a bidirectional road between cities `ai` and `bi` with a distance of `distance_i`.

A **path** from city `1` to city `n` is a sequence of roads connecting these two cities.

Your task is to return the **minimum score** of any path between city `1` and city `n`, where the **score** of a path is defined as the **minimum distance of any edge** in that path.

---

### Example 1:
* **Input**: `n = 4`, roads = `[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]`  
* **Output**: `5`  
* **Explanation**: One of the paths from 1 to 4 is [1, 2, 4] with edge weights 9 and 5 → score is `min(9, 5) = 5`.

### Example 2:
* **Input**: `n = 2`, roads = `[[1,2,2]]`  
* **Output**: `2`  
* **Explanation**: Only one road connects the cities.

---

### Constraints:
* `2 <= n <= 10^5`
* `1 <= roads.length <= 10^5`
* `roads[i].length == 3`
* `1 <= ai, bi <= n`
* `ai != bi`
* `1 <= distance_i <= 10^4`
* There are no repeated edges.
* The graph is connected.

---

## Solution

We use the **Union-Find (Disjoint Set Union)** structure to group cities into connected components.  
While merging components, we also track the **minimum edge weight** seen within each component.

At the end, the answer is the **minimum edge weight in the component that contains city 1**, since the graph is connected and we can reach any node from node 1.

---

### Key Observations:

- The graph is connected, so there will always be a path from city 1 to city `n`.
- The "score" of a path is determined by the smallest edge in that path.
- Since all cities are connected, we only care about the **minimum edge** in the component of city `1`.

---

### Steps:

1. Initialize a Union-Find structure with `n` cities.
2. For each road, union the two cities and update the minimum weight in their component.
3. After processing all roads, return the minimum weight in the component containing city `1`.

---

### Time and Space Complexity:

- **Time Complexity**: `O(E * α(N))`, where `E` is the number of roads and `α(N)` is the inverse Ackermann function (almost constant in practice).
- **Space Complexity**: `O(N)` — for Union-Find arrays (`parent`, `size`, `weight`).

---
