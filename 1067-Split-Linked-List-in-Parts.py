from typing import (
    List,
)

class Solution:
    """
    @param root: the list
    @param k: the split sum
    @return: the answer
    """
    def split_linked_listin_parts(self, root: List[int], k: int) -> List[List[int]]:
        n = len(root)
        res = [[] for i in range(k)]

        # 情况1
        # root = [1, 2, 3], k = 5
        # 输出: [[1],[2],[3],[],[]]
        if n // k == 0:
            for i in range(n):
                res[i].append(root[i])
            return res
        
        # 情况2
        # root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 2
        # 输出: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        if n % k == 0:
            l = n // k # 每段的长度
            for i in range(k):
                res[i].extend(root[i*l:(i+1)*l])
            return res
        
        # 情况3
        # root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
        # 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        extra = n - n // k * k
        l = n // k # 每段的长度
        for i in range(extra):
            res[i].extend(root[i*(l+1):(i+1)*(l+1)])
        for i in range(extra, k): # extra*(l+1)是跳过的部分，在用i-extra归零
            res[i].extend(root[extra*(l+1) + (i-extra  ) * l:\
                               extra*(l+1) + (i-extra+1) * l])
        return res
