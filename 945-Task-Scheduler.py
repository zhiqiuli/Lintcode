'''
AAA BBB

M=3

1. (M-1)*N idle time
2. execute itself for M times
3. (M-1)*N + M
4. extra elements (Mct-1). in the following case it is BCD
   AAA BBB CCC DDD => ABCD|ABCD|ABCD|A|BCD
'''

class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def least_interval(self, tasks: str, n: int) -> int:
        d = collections.Counter(tasks)
        counts = list(d.values())
        longest = max(counts)
        # AAABBB and n=1 -> longest = 3
        ans = (longest - 1) * (n + 1) + counts.count(longest)
        return max(len(tasks), ans)
