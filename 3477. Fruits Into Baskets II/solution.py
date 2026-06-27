class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        occupiedBaskets = set()
        for fruit in fruits:
            for ind in range(len(baskets)):
                if baskets[ind] >= fruit and ind not in occupiedBaskets:
                    occupiedBaskets.add(ind)
                    break
            else:
                count += 1
        
        return count
