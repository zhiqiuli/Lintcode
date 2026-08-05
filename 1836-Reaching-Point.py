from typing import (
    List,
)

class Solution:
    """
    @param start: a point [x, y]
    @param target: a point [x, y]
    @return: return True or False
    """
    def reaching_points(self, start: List[int], target: List[int]) -> bool:
        sx, sy = start[0], start[1]
        tx, ty = target[0], target[1]
        # 同时满足以下三个条件，进行反向计算
        # mod的操作可以想象成这样(7,100) -> (7, 93) -> (7,86) ... -> (7, 2)
        while tx > sx and ty > sy and tx != ty:
            if tx > ty:
                tx = tx % ty
            elif tx < ty:
                ty = ty % tx
        
        # 找到答案
        if sx == tx and sy == ty:
            return True
        # 如果tx=sx且ty≠sy，则tx不能继续减小，只能减小ty，因此只有当ty>sy且(ty−sy)%tx==0时可以从起点转换到终点。
        if sx == tx and sy != ty:
            return ty > sy and (ty - sy) % tx == 0
        if sx != tx and sy == ty:
            return tx > sx and (tx - sx) % ty == 0
        # 如果tx≠sx且ty≠sy，则不可以从起点转换到终点。
        # if sx != tx and sy != ty:
        #     return False
        return False