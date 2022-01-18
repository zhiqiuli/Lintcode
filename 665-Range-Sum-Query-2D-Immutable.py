class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        # do intialization if necessary
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                 self.prefix_sum[i][j] = - self.prefix_sum[i-1][j-1] + self.prefix_sum[i][j-1] + self.prefix_sum[i-1][j] + matrix[i-1][j-1]
        # print(self.prefix_sum)
        
    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        # write your code here
        return - self.prefix_sum[row2 + 1][col1    ] \
               - self.prefix_sum[row1    ][col2 + 1] \
               + self.prefix_sum[row1    ][col1    ] \
               + self.prefix_sum[row2 + 1][col2 + 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
