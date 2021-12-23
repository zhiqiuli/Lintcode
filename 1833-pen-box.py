class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimumBoxes(self, boxes, target):
        if not boxes or len(boxes) < 2 or not target or target < 0:
            return -1 
        left_min = self.get_min_len(boxes, target) # 左侧的最优解是什么
        #print(left_min)
        new_boxes = boxes[::-1]
        right_min = self.get_min_len(new_boxes, target) 
        right_min = right_min[::-1] # 右侧的最优解是什么
        #print(right_min)
        ans = sys.maxsize
        n = len(boxes)
        for i in range(n - 1):
            if left_min[i] == sys.maxsize or right_min[i + 1] == sys.maxsize: # 必须加上这条因为题目要求找到两个区间
                continue
            ans = min(ans, left_min[i] + right_min[i + 1])
        if ans == sys.maxsize:
            return -1
        return ans 
    
    def get_min_len(self, boxes, target):
        ans = []
        left = now_sum = 0
        length = sys.maxsize
        n = len(boxes)
        for right in range(n):
            now_sum += boxes[right]
            while now_sum > target:
                now_sum -= boxes[left]
                left += 1 
            if now_sum == target:
                length = min(length, right - left + 1)
            ans.append(length)
        return ans
