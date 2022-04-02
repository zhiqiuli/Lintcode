class Solution:
    """
    @param s: the given string
    @return: the minimum number of parentheses we must add
    """
    def min_add_to_make_valid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                stack.append('*')
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    # count how many extra )'s
                    count += 1
        # stack counts extra ('s
        return len(stack) + count
