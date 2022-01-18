class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A:
            return True
        
        dp = [False] * len(A)
        dp[0] = True

        for i in range(len(A)):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
        
        return dp[-1]
        
        
        
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if len(A) == 0:
            return 0
        maxJump, i = A[0], 0
        while i < len(A):
            if maxJump >= len(A) - 1:
                return True
            if maxJump == i :
                return False
            if i < maxJump:
                maxJump = max(i+A[i], maxJump)
                i += 1

        return False
