class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_count = Counter(digits)
        valid_count = 0
        
        for num in range(100, 1000, 2):
            needed_count = Counter(int(d) for d in str(num))
            
            if all(digit_count[d] >= needed_count[d] for d in needed_count):
                valid_count += 1
                
        return valid_count
