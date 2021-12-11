import math
class Solution:
    """
    @param deck: a integer array
    @return: return a value of bool
    """
    def hasGroupsSizeX(self, deck):
        res = [ 0 ] * 10001
        for val in deck:
            res[val] += 1
        res_set = set(res)
        res_set.remove(0)
        return math.gcd(*list(res_set)) > 1
