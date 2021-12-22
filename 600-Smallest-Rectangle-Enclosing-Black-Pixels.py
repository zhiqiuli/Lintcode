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

