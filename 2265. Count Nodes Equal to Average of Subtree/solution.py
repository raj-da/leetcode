# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                return [0, 0]
            
            valSum, count = node.val, 1
            left, right = dfs(node.left), dfs(node.right)
            
            valSum += left[0] + right[0]
            count += left[1] + right[1]

            result += int(node.val == valSum // count)
            
            return [valSum, count]
        
        dfs(root)

        return result
