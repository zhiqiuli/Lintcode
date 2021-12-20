class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)

    def sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
        
        color = (color_from + color_to ) // 2 # partition在color上，所以是NlogK的时间复杂度

        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color: # 左边实际上排序的是[color_from, color]
                left += 1
            while left <= right and colors[right] > color: # 右边实际上排序的是[color+1, color_to]
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left  += 1
                right -= 1
        
        self.sort(colors, color_from, color   , index_from, right   )
        self.sort(colors, color + 1 , color_to, left      , index_to)
