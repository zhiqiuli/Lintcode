class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        if not s:
            return [""]
        queue = collections.deque([s])
        visited = set([s])
        res = []
        found = False
        while queue:
            q = queue.popleft()
            if self.is_valid(q):
                found = True
                res.append(q)
            # - If found, which means current level has all the solutions
            #   then no need to moving into next level.
            # - If not found, go to next level.
            elif not found:
                for i in range(len(q)):
                    # everytime remove either a ( or a )
                    if q[i] == '(' or q[i] == ')':
                        q_new = q[:i] + q[i+1:]
                        if q_new not in visited:
                            queue.append(q_new)
                            visited.add(q_new)
        return res
   
    # check if a given string s with valid parenthesis
    def is_valid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append('*')
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
            else:
                continue
        return not stack
