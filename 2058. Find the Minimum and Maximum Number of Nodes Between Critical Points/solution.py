# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prevNode, curNode = None, head
        minDistance, maxDistance = inf, -1

        leftInd, prevInd = -1, -1
        ind = 0
        while curNode:
            if prevNode and curNode.next:
                if (prevNode.val < curNode.val > curNode.next.val) or (prevNode.val > curNode.val < curNode.next.val):
                    if prevInd > 0:
                        minDistance = min(minDistance, ind - prevInd)
                    
                    if leftInd > 0:
                        maxDistance = ind - leftInd
                    else:
                        leftInd = ind
                    
                    prevInd = ind
           
            ind += 1 
            prevNode = curNode
            curNode = curNode.next
        
        minDistance = minDistance if minDistance < 10**5 else -1
        return [minDistance, maxDistance]
