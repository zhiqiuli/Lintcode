# https://www.lintcode.com/problem/382/description?_from=collection&fromId=161

'''
triangle inequality 说*短边*之和要大于长边。。。如果满足sorted array a<=b<=c 就只需要看 a+b > c就可以
'''
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if not S:
            return 0
        S.sort()
        count = 0
        for i in range(2, len(S)): # S[i] is the 3rd side, so if and only if S[left] + S[right] > S[i] is OK
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        
        return count

