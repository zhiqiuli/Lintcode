class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        A = sorted(A) # 排序能保证结果和答案一致
        res = []
        self.dfs(A, k, target, [], res, 0)
        return res
    
    def dfs(self, A, k, target, chars, res, start):
        # 递归出口 都是正数 所以不可能小于0
        if target < 0:
            return
        # 长度到k时 保存结果或者退出
        if len(chars) == k:
            # 保存结果
            if target == 0:
                res.append(chars[:])
            return
        
        for i in range(start, len(A)):
            chars.append(A[i])
            self.dfs(A, k, target - A[i], chars, res, i + 1)
            chars.pop()
