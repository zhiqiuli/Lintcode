class Solution:
    """
    @param pairs: pairs of numbers
    @return: the length longest chain which can be formed
    """
    def findLongestChain(self, pairs):
        # 这个题目的关键就是根据第二个元素来排序
        pairs = sorted(pairs, key = lambda x:x[1])
        longest, curr_right = 0, -sys.maxsize
        print(pairs)
        for left, right in pairs:
            if left <= curr_right:
                continue
            curr_right = right
            longest += 1
        return longest
