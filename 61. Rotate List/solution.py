# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeCount = 0

        # count number of node
        curNode = head
        lastNode = None
        while curNode:
            lastNode = curNode
            nodeCount += 1
            curNode = curNode.next
        
        k %= nodeCount
        if k == 0:
            return head
        
        cur = head
        for _ in range(nodeCount - k - 1):
            cur = cur.next
        
        nxt = cur.next
        cur.next = None
        lastNode.next = head


        return next
