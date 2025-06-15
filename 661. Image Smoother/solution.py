class Solution:
    def is_in_bounds(self, rows, cols, r, c):
        """
        Checks if (r, c) is within the boundaries of the image.
        """
        return 0 <= r < rows and 0 <= c < cols

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        # Initialize the smoothed image with the same dimensions
        smoothed_img = [[0] * cols for _ in range(rows)]

        # Directions for 8 neighboring cells: up, down, left, right, and 4 diagonals
        directions = [
            (0, 1),  # right
            (0, -1),  # left
            (1, 0),  # down
            (-1, 0),  # up
            (1, 1),  # bottom-right
            (-1, -1),  # top-left
            (1, -1),  # bottom-left
            (-1, 1),  # top-right
        ]

        # Traverse each pixel in the original image
        for r in range(rows):
            for c in range(cols):
                pixel_sum = img[r][c]  # Start with the current pixel
                count = 1  # Count includes the current pixel

                # Add valid neighboring pixel values
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if self.is_in_bounds(rows, cols, new_r, new_c):
                        pixel_sum += img[new_r][new_c]
                        count += 1

                # Compute average and assign to smoothed image
                smoothed_img[r][c] = pixel_sum // count

        return smoothed_img

        # Time Complexity: O(n * m), where n = number of rows, m = number of columns
        # Space Complexity: O(n * m) for the output image
