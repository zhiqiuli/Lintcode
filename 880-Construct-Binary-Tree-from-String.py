"""
递归 + 栈。栈用来匹配括号，分成左右两个子树。这里默认 str 是格式正确的，所以要预先去掉首尾的 ()。
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        #print(s)
        if not s: return None

        # end case - no ( in the string
        if '(' not in s:
            return TreeNode(int(s))
        
        # find the root first
        idx = s.index('(')
        root = TreeNode(int(s[:idx]))
        stk, idx = ['('], idx + 1
        start = idx

        while stk:
            if s[idx] == '(':
                stk.append('(')
            elif s[idx] == ')':
                stk.pop()
            idx += 1
        
        print('left + ', s[:idx])
        print('right + ', s[idx+1:])

        root.left  = self.str2tree(s[start:idx-1])
        root.right = self.str2tree(s[idx+1:-1])

        return root
