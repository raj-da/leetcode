# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0

        que = deque([root])
        while que:
            node = que.popleft()
            if low <= node.val <= high:
                result += node.val
            
            if node.left:
                que.append(node.left)
            
            if node.right:
                que.append(node.right)
        
        return result
