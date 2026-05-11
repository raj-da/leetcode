class Solution:
    def separate(self, num):
        digits = []
        while num > 0:
            digits.append(num%10)
            num //= 10

        digits.reverse()
        return digits

    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            if i <= 9:
                answer.append(i)
            else:
                answer.extend(self.separate(i))

        return answer
