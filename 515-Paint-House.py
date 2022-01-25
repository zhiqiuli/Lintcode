class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        costs_up_to = [[0, 0, 0] for _ in range(len(costs) + 1)]
        for i in range(1, len(costs) + 1):
            # the costs up to the ith house when painting ith house using color 0, 1 or 2
            costs_up_to[i][0] = costs[i-1][0] + min(costs_up_to[i-1][1], costs_up_to[i-1][2])
            costs_up_to[i][1] = costs[i-1][1] + min(costs_up_to[i-1][0], costs_up_to[i-1][2])
            costs_up_to[i][2] = costs[i-1][2] + min(costs_up_to[i-1][0], costs_up_to[i-1][1])
        return min(costs_up_to[-1])
