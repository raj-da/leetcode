class Solution(object):
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        m = s + s 
        return m.find(goal) != -1
        
        # Time complexity: O(n*n)
        # Space complexity: O(n)
