class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        sortedVowel = deque(sorted([char for char in s if char in vowels]))

        result = []
        for char in s:
            if char in vowels:
                result.append(sortedVowel.popleft())
            else:
                result.append(char)
        
        return ''.join(result)
