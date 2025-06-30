class Solution:
    def simplifyPath(self, path: str) -> str:
        simple_path = []  # stack to keep track of the valid directories
        current_path = path.split('/')  # split input path by '/'

        for symbol in current_path:
            if symbol == "..":
                # move one directory back if it exists
                if simple_path:
                    simple_path.pop()
            elif symbol and symbol != '.':
                # skip empty and '.' (current directory)
                simple_path.append(symbol)

        # build the simplified path
        return '/' + '/'.join(simple_path)
    
# Time-Complexity: O(n)
# Space-Complexity: O(n)