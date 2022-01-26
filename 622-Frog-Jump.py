'''
解题思路
本题使用动态规划的思路。
数据结构采用散列表（hashmap），对于{key:value}键值对，key表示石头的位置，value是step的集合，step表示青蛙上次跳动到这里时用的步数。
对于每块石头，已知跳到这里用了step步，那么就看从该位置跳step-1、step和step+1能不能跳到新的石头，如果可以，在新的石头的value处加入这个步数。

算法流程
首先，处理corner case。石头数量少于两块，返回true；前两块石头的位置不是0和1，返回false。
初始化散列表dp，key是石头的位置，相应的value设为空集。将dp[0]设置为{1}，表示从第0块石头只能跳1步。
对于每块石头的位置stone，我们遍历dp[stone]得到上一块石头跳到这块石头的步数step。那么接下来它就可以跳step-1或step或step+1步，我们检查这三个位置有无石头。假如有石头，就在其相应的value集合中加入相应的步数。
然后前往下块石头的位置继续上述操作。

复杂度分析
时间复杂度：O(n^2)O，n为stones数组的大小。双重循环。
空间复杂度： O(n^2)，散列表最大为 n^2。
'''

class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        if len(stones) <= 1:
            return True
        # 初始化dp数组
        dp = {stone: set() for stone in stones}
        dp[0].add(1) # 使用dp[0].add(0)也能通过
        for stone in stones:
            for step in dp[stone]:
                # 跳跃 step - 1，注意and后的条件确保不会倒退到之前的位置
                if (stone + step - 1 in dp) and (stone + step - 1 > stone):
                    dp[stone + step - 1].add(step - 1)
                # 跳跃 step
                if stone + step in dp:
                    dp[stone + step].add(step)
                # 跳跃 step + 1
                if stone + step + 1 in dp:
                    dp[stone + step + 1].add(step + 1)
        return len(dp[stones[-1]]) > 0
