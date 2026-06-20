# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        hasParent = defaultdict(lambda:False)
        for parent, child, isLeft in descriptions:
            childNode = nodes[child] if child in nodes else TreeNode(child)
            parentNode = nodes[parent] if parent in nodes else TreeNode(parent)
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            
            nodes[child] = childNode
            nodes[parent] = parentNode

            hasParent[child] = True
        
        
        for node, _, _ in descriptions:
            if hasParent[node] == False:
                return nodes[node]
