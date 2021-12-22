###
### BFS
###
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        minx, miny, maxx, maxy = x, y, x, y
        visited = set([(x, y)])
        queue = collections.deque([(x,y)])
        while queue:
            curx, cury = queue.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                newx = curx + dx
                newy = cury + dy
                if self.isValid(newx, newy, visited, image):
                    queue.append((newx, newy))
                    visited.add((newx, newy))
                    minx,miny,maxx,maxy = min(minx,newx),min(miny,newy),max(maxx,newx),max(maxy,newy)
        return (maxx-minx+1) * (maxy-miny+1)
    
    def isValid(self, x, y, visited, image):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return False
        if (x, y) in visited or image[x][y] == '0':
            return False
        return True


    ###
    ### 二分法
    ###
    class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        m, n = len(image), len(image[0])
        left  = self.bs(0    , x, image, self.is_row_empty)
        right = self.bs(m - 1, x, image, self.is_row_empty)
        bot   = self.bs(0    , y, image, self.is_col_empty)
        top   = self.bs(n - 1, y, image, self.is_col_empty)
        return (right - left + 1) * (top - bot + 1)
    
    def bs(self, start, end, G, is_empty):
        if start < end:
            check = lambda start, end: start + 1 < end
        else:
            check = lambda start, end:   end + 1 < start
        
        while check(start, end):
            mid = (start + end) // 2
            if is_empty(G, mid):
                end = mid
            else:
                start = mid

        return start if is_empty(G, start) else end
    
    # 给定row x 判断是否存在1
    def is_row_empty(self, G, x):
        for cell in G[x]:
            if cell == '1':
                return True
        return False

    # 给定col y 判断是否存在1
    def is_col_empty(self, G, y):
        for cell in G:
            if cell[y] == '1':
                return True
        return False
