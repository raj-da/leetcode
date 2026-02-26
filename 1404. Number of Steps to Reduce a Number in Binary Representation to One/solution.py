class Solution:
    def numSteps(self, s: str) -> int:
        que = deque(s)
        
        def divide():
            que.pop()
        
        def addOne():
            ind = len(que) - 1
            while ind >= 0 and que[ind] == '1':
                que[ind] = '0'
                ind -= 1
            if ind >= 0:
                que[ind] = '1'
            else:
                que.appendleft('1')

        steps = 0
        while len(que) > 1 or que[0] != '1':
            if que[len(que)-1] == '1':
                addOne()
            else:
                divide()
            steps += 1

        return steps
