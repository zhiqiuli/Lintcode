class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, A):
        if A == []:
            return 0
        index = 0
        for i in range(1, len(A)):
            if A[index] != A[i]:
                index += 1
                A[index] = A[i]
        return index + 1
