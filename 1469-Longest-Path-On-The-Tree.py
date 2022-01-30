'''
简单解法，大佬们思路的翻译机。

思路：

随便一点找最远
最远的点找最远
解法：

第一次BFS，找第一个点的最远。
第二次BFS，找找到的最远的点的最远。
BFS迭代的时候记录最长路径，最长路径打擂台。
想法：

这个题更接近DFS的感觉，但是可以用BFS来迭代。
DFS需要递归的次数为树的最大长度，有可能会爆栈。
复杂度：

时间：O(E) 所有Edge都处理一次
空间：O(N) visited，所有节点记录一次
优化：

1维数组代替visited dict，速度从beats 20% 提升到 80%。
据大佬说速度数组 vs 字典，速度x3
数组的话空间 O(N) == O(10^5)
'''
class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longestPath(self, n, starts, ends, lens):
        
        # Defaultdict is a container like dictionaries present in the module collections.
        # Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object.
        # The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError.
        # It provides a default value for the key that does not exists.
        edges = collections.defaultdict(list)
        for i in range(len(starts)):
            edges[starts[i]].append((starts[i], ends[i], lens[i]))
            edges[ends[i]].append((ends[i], starts[i], lens[i]))

        # from any of the node to find it's longest path.
        queue = collections.deque([(0, 0)])
        visited = [0] * 10 ** 5
        visited[0] = 1
        start_at = 0
        max_length = 0
        while queue:
            n, sum_length = queue.popleft()

            max_length = max(max_length, sum_length)
            if max_length == sum_length:
                start_at = n
            
            for st, ed, edge_len in edges[n]:
                if visited[ed]:
                    continue
                
                visited[ed] = 1
                queue.append((ed, sum_length + edge_len))
        
        
        # from start node to longest path
        queue = collections.deque([(start_at, 0)])
        visited = [0] * 10 ** 5
        visited[start_at] = 1
        end_at = 0
        ret = 0
        while queue:
            n, sum_length = queue.popleft()

            ret = max(ret, sum_length)

            for st, ed, edge_len in edges[n]:
                if visited[ed]:
                    continue

                visited[ed] = 1
                queue.append((ed, sum_length + edge_len))

        return ret
