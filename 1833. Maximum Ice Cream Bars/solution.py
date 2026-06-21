class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        frequency = [0]*(max(costs) + 1)
        for cost in costs:
            frequency[cost] += 1
        
        count = 0
        for ind, freq in enumerate(frequency):
            for _ in range(freq):
                if coins < ind:
                    return count
                count += 1
                coins -= ind
        
        return count
