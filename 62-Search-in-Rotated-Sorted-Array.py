# https://www.lintcode.com/problem/62/description

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        
        start, end = 0, len(A) - 1

        while start + 1 < end:

            mid = start + int((end - start) / 2)

            # case 1 when mid (^) is on the 1st part
            # 4 5 6 7 1 
            #     ^
            if A[mid] >= A[start]: # 如果第一部分是递增的
                # case 1.1 when target (@) is on the 1st part of 1st part
                # 4 5 6 7 1 
                #   @ ^
                if A[start] <= target <= A[mid]: # target就在第一部分递增的里面 直接使用模版的end
                    end = mid
                # case 1.2 when mid is on the 2nd part of 1st part
                else:
                    start = mid
            # case 2 when mid is on the 2nd part # 如果第二部分是递增的
            else:
                if A[mid] <= target <= A[end]: # target在第二部分递增的里面 
                    start = mid
                else:
                    end = mid
        
        if A[start] == target: # 需要严格等于
            return start
        if A[end] == target: # 需要严格等于
            return end
        
        return -1
