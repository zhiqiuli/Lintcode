import copy

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        init_state_str  = self.state2str(init_state)
        final_state_str = self.state2str(final_state)

        visited = set([init_state_str])
        queue   = collections.deque([init_state_str])
        step    = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == final_state_str:
                    return step
                nbs = self.getNeighborMatrix(node)
                for nb in nbs:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            step += 1
        return -1

    def state2str(self, state):
        s = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                s.append(str(state[i][j]))
        return ''.join(s)
    
    # get neighboring matrices
    # check if the neighbor matrix is valid
    def getNeighborMatrix(self, cur_state):
        zeroIndex = cur_state.index('0')
        x, y = zeroIndex // 3, zeroIndex % 3
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nIndex = nx * 3 + ny
                cur_state_list = list(cur_state)
                cur_state_list[zeroIndex], cur_state_list[nIndex] = cur_state_list[nIndex], cur_state_list[zeroIndex]
                neighbors.append(''.join(cur_state_list))
        return neighbors
