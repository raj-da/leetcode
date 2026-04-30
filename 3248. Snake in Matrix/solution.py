class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        for command in commands:
            match command:
                case 'RIGHT':
                    j += 1
                case 'LEFT':
                    j -= 1
                case 'UP':
                    i -= 1
                case 'DOWN':
                    i += 1
          
        return (i * n) + j
