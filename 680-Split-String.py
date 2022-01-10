class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, index, path, res):
        # remove the case 
        if index > len(s):
            return

        # save the results
        if index == len(s):
            res.append(path[:])
            return
        
        # one charater        
        path.append(s[index:index+1])
        self.dfs(s, index+1, path, res)
        path.pop()

        # two charaters
        path.append(s[index:index+2])
        self.dfs(s, index+2, path, res)
        path.pop()
