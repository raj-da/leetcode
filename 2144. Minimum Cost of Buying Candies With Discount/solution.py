class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse=True)
        
        minCost = 0
        ind = 0
        while ind < n:
            minCost += cost[ind] + (cost[ind+1] if ind + 1 < n else 0)
            ind += 3
        
        return minCost
