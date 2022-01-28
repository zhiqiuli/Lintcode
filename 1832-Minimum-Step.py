class Solution:
    """
    @param colors: the colors of grids
    @return: return the minimum step from position 0 to position n - 1
    """
    def minimumStep(self, colors):
        n = len(colors)
        min_step = {}
        visited_grid = set()
        visited_color = set()

        # 按颜色分类，每个颜色占了哪些space
        color_group = [[] for _ in range(n + 1)]
        for i in range(n):
            color_group[colors[i]].append(i)
        
        queue = collections.deque([0])
        min_step[0] = 0
        visited_grid.add(0)
        # visited_color.add(colors[0])

        while queue:
            pos = queue.popleft()
            color = colors[pos]
            # 如果某个颜色未处理过，先处理这个颜色
            if color not in visited_color:
                visited_color.add(color)
                for newPos in color_group[color]:
                    if self.is_valid(n, newPos, visited_grid):
                        min_step[newPos] = min_step[pos] + 1
                        queue.append(newPos)
                        visited_grid.add(newPos)
            
            # 左右移动的情况 此时不用考虑颜色的问题 颜色在之前一部分处理
            for newPos in [pos + 1, pos - 1]:
                if self.is_valid(n, newPos, visited_grid):
                    min_step[newPos] = min_step[pos] + 1
                    queue.append(newPos)
                    visited_grid.add(newPos)
            
        return min_step[n - 1]

    def is_valid(self, n, pos, visited_grid):
        if pos < 0 or pos >= n:
            return False
        if pos in visited_grid:
            return False
        return True
