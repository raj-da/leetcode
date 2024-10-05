class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        l = 0

        if len(s1) > len(s2):
            return False

        # Time complexity: O(n) for n = len(s1)
        for i in s1:
            count1[i] = 1 + count1.get(i, 0)

        # creating the window
        # Time complexity: O(n)
        for r in range(len(s1)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)

        if count1 == count2:
            return True

        # Time complexity: O(m - n) for m = len(s2)
        for r in range(len(s1), len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                count2.pop(s2[l])
            l += 1

            if count1 == count2:
                return True

        return False
    

# Time complexity O(n + m) , n = len(s1), m = len(s2)
# Space complexity O(2k), k = len(s1)
