class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        if not num: return []
        num = sorted(num)
        res = []
        self.dfs(num, 0, target, [], res)
        return res
    
    def dfs(self, num, index, target, path, res):
        if target == 0:
            res.append(path[:])
            return

        for i in range(index, len(num)):
            if target - num[i] < 0:
                break
            # [1,2',2",3] 5 -> [2',3] do not use [2",3]
            if i != index and num[i] == num[i - 1]:
                continue
            path.append(num[i])
            self.dfs(num, i + 1, target - num[i], path, res)
            path.pop()

