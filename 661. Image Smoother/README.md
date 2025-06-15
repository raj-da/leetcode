# [661. Image Smoother](https://leetcode.com/problems/image-smoother/)
**Difficulty:** <span style="color: green">Easy</span>

## Problem Description

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the surrounding 8 cells. 

You are given an `m x n` integer matrix `img` representing the grayscale of an image, where `img[i][j]` represents the value of the pixel at row `i` and column `j`.

To apply the smoother, replace each `img[i][j]` with the average (rounded down) of all the valid surrounding cells including itself.

Return *the resulting image as a 2D matrix*.

---

### Example 1:

**Input:**  
`img = [[1,1,1],[1,0,1],[1,1,1]]`

**Output:**  
`[[0,0,0],[0,0,0],[0,0,0]]`

---

### Example 2:

**Input:**  
`img = [[100,200,100],[200,50,200],[100,200,100]]`

**Output:**  
`[[137,141,137],[141,138,141],[137,141,137]]`

---

### Constraints:

- `m == img.length`
- `n == img[i].length`
- `1 <= m, n <= 200`
- `0 <= img[i][j] <= 255`

---

## My Solution:

1. **Iterate** over every cell in the matrix.
2. For each cell, **check all 8 neighbors** (and itself).
3. **Sum the values** of valid neighbors (cells within bounds).
4. Compute the **average** (rounded down using floor division).
5. Store the result in a **new matrix** of the same size.
6. Return the new matrix.