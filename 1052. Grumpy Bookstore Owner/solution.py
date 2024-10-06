class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Step 1: calculate base total satisfaction without grumpy time
        total_satisfaction = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfaction += customers[i]

        
        # Step 2: Sliding window to find max additional satisfaction we can get
        max_additional, additional = 0, 0

        # Creating the window
        for r in range(minutes):
            if grumpy[r] == 1:
                additional += customers[r]

        max_additional = additional

        # Sliding the window over the rest of the array
        for r in range(minutes, len(customers)):
            if grumpy[r] == 1:
                additional += customers[r] # Add the new customer at the end of the window
            
            if grumpy[r - minutes] == 1:
                additional -= customers[r - minutes] # Remove the customer that is out of the window

            max_additional = max(max_additional, additional)

        return total_satisfaction + max_additional
    

# Time Complexity: O(n), n = len(customers)
# Space Complexity: O(1) 