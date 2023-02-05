from typing import (
    List,
)

class Solution:
    """
    @param num: a array
    @param target: a num
    @return: return all combinations
             we will sort your return value in output
    """
    def combination_set(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        res = []
        self.dfs(nums, [], res, target)
        return res

    def dfs(self, nums, path, res, target):

        if path:
            ans = int(''.join(path))
            if ans >= target:
                return
            else:
                res.append(ans)

        for num in nums:

            # prune cases starting with 0, such as 01, 02, ... but keep the case 0
            if path and path[0] == '0':
                continue
                
            path.append(str(num))
            self.dfs(nums, path, res, target)
            path.pop()