class Solution:
	    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # 找到 A[left] < target, A[right] >= target
        # 也就是最接近 target 的两个数，他们肯定是相邻的
        right = self.findUpperClosest(A, target)
        left = right - 1
 
 
         # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        res = []
        for _ in range(k):
            if self.isLeftCloser(A, left, right, target):
                res.append(A[left])
                left -= 1
            else:
                res.append(A[right])
                right += 1
       
        return res
   
# 标准二分法模版
# 找的是xxxxx(v)vvvvv，所以A[mid]>=target: right = mid
    def findUpperClosest(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            if A[mid] >= target:
                right = mid
            else:
                left = mid
        if A[left] >= target:
            return left
        if A[right] >= target:
            return right
       
        # 找不到的情况
        return len(A)
   
    def isLeftCloser(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] – target # 相同的话，那么小的数排在前面，所以左移动
