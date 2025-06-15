# [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/)  
**Difficulty:** <span style = "color : red">Hard</span>

## Problem Description

You are given an `n x n` binary matrix `grid`. You can change **at most one** `0` to be `1`.  
After this change, what is the size of the largest island in `grid`?  
An **island** is a 4-directionally connected group of `1`s.

Return the size of the largest island possible after changing at most one `0` to `1`.

---

### Example 1:
* **Input**: `grid = [[1,0],[0,1]]`  
* **Output**: `3`  
* **Explanation**: Change one of the 0s to 1 to connect the two 1s.

### Example 2:
* **Input**: `grid = [[1,1],[1,0]]`  
* **Output**: `4`  
* **Explanation**: Change the 0 to 1 to form a full 2x2 island.

### Example 3:
* **Input**: `grid = [[1,1],[1,1]]`  
* **Output**: `4`  
* **Explanation**: No need to flip any 0 since all are already 1.

---

### Constraints:
* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 500`
* `grid[i][j]` is either `0` or `1`.

---

## Solution

We use the **Union-Find (Disjoint Set Union)** data structure to group 1s into islands.  
Each island is assigned a unique representative, and we maintain the size of each group.

Then for each `0` cell, we simulate flipping it to `1` and look at its 4 neighbors.  
We compute the potential size of the island by adding the sizes of all **unique neighboring islands**.

The answer is the maximum of all such possible sizes.

---

### Key Observations:

- An island is a connected component of 1s.
- We only need to check `0` cells and try flipping them to see what maximum size island we can form.
- Avoid double-counting neighboring islands by using a `set` of unique parents.

---

### Steps:

1. Use DFS and Union-Find to group all `1`s into islands.
2. For every `0`, check its 4-directional neighbors and collect their island parents.
3. Sum the sizes of those unique islands and add 1 (for the flipped cell).
4. Return the maximum island size found.

---

### Time and Space Complexity:

- **Time Complexity**: `O(n^2)` — each cell is visited once for DFS and for the check.
- **Space Complexity**: `O(n^2)` — for parent and size maps in Union-Find.

---
