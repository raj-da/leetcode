class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        interval_intersection = []
        n, m = len(firstList), len(secondList)
        i, j = 0, 0

        # Traverse both interval lists using two pointers
        while i < n and j < m:
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # Check for an overlap between intervals
            if a_start <= b_end and b_start <= a_end:
                # Compute and add the intersection of the overlapping intervals
                interval_intersection.append([max(a_start, b_start), min(a_end, b_end)])

            # Move the pointer for the interval that ends first
            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return interval_intersection

# Time-Complexity: O(n + m)
# Space-Complexity: O(1)