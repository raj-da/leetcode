class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7:
            return 0

        mydict = {'b':0, 'a': 0, 'l':0, 'o':0, 'n': 0}

        for i in text:
            if i in ['b', 'a', 'l', 'o', 'n']:
                mydict[i] += 1 

        mydict['l'] //= 2
        mydict['o'] //= 2

        return min(mydict.values())
