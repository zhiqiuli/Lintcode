class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplify_path(self, path: str) -> str:
        levels = path.split('/')
        stack = []
        for level in levels:
            if level == '.' or level == '':
                continue
            elif level == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(level)
        print(levels)
        print(stack)
        return '/' + '/'.join(stack)
