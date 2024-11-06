class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        m = s + s 
        return m.find(goal) != -1
        
        # Time complexity: O(n*n)
        # Space complexity: O(n)