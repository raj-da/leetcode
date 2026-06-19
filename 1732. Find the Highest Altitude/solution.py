class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxGain = 0
        curGain = 0
        for ga in gain:
            curGain += ga
            maxGain = max(maxGain, curGain)
        
        return maxGain
