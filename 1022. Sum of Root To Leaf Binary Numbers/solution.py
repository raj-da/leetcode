# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int: 
        result = 0
        def dfs(node, bits):
            nonlocal result
            bits += str(node.val)
            if (not node.right) and (not node.left):
                result += int(bits,2)
                return
            
            if node.left:
                dfs(node.left, bits)
            if node.right:
                dfs(node.right, bits)

        dfs(root, "")
        return result
