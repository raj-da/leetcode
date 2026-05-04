class Solution {
  void rotate(List<List<int>> matrix) {
    int rows = matrix.length;
    int cols = rows;

    // Transpose the matrix.
    for (int r = 0; r < rows; r++) {
        for (int c = r; c < cols; c++) {
            int temp = matrix[r][c];
            matrix[r][c] = matrix[c][r];
            matrix[c][r] = temp;
        }
    }

    // Reverse each row.
    for (int r = 0; r < rows; r++) {
        int left = 0;
        int right = rows - 1;
        // Reverse a row
        while (left < right) {
            int temp = matrix[r][left];
            matrix[r][left] = matrix[r][right];
            matrix[r][right] = temp;
            left++;
            right--;
        }
    }
  }
}

// Time complexity: O(n*n)
// Space complexity: O(1)
