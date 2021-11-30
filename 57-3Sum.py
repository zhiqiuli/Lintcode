# https://www.lintcode.com/problem/57/description?_from=collection&fromId=161

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 2:
            return []
        
        numbers.sort()
        res = []

        # c goes from 0 to len(numbers) - 2
        for i in range(len(numbers) - 2):
            # remove duplicated cases if c's are all the same
            if i and numbers[i] == numbers[i-1]:
                continue
            c = numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left < right:
                s = numbers[left] + numbers[right] + c
                if s == 0:
                    res.append([numbers[i], numbers[left], numbers[right]])
                    left  += 1
                    right -= 1
                    while left < right and numbers[left]  == numbers[left  - 1]:
                        left  += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left  += 1
        
        return res
