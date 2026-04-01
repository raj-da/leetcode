class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[ind], healths[ind], directions[ind], ind] for ind in range(n)]

        robots.sort(key=lambda robot: (robot[0], robot[-1])) # sort by position and then by index
        stack = []

        # print(robots)
        for robot in robots:
            stack.append(robot)
            while (len(stack) > 1) and (stack[-2][2] == 'R' and stack[-1][2] == 'L'):
                toLeftRobot = stack.pop()
                toRightRobot = stack.pop()

                healthDiff = toRightRobot[1] - toLeftRobot[1]
                
                if healthDiff > 0:
                    toRightRobot[1] -= 1
                    stack.append(toRightRobot)
                elif healthDiff < 0:
                    toLeftRobot[1] -= 1
                    stack.append(toLeftRobot)
        
        stack.sort(key=lambda x: x[-1])
        return [robot[1] for robot in stack]
