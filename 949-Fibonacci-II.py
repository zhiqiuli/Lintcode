class Matrix:
	def __init__(self):
		self.mat = [[0 for j in range(2)] for i in range(2)]
	def __mul__(self, m):
		tmp = Matrix()
		for i in range(2):
			for k in range(2):
				if(self.mat[i][k] == 0):
					continue
				for j in range(2):
					tmp.mat[i][j] += self.mat[i][k] * m.mat[k][j]
					tmp.mat[i][j] %= 10000;
		return tmp
	def unit(self):
		for i in range(2):
			for j in range(2):
				if i == j:
					self.mat[i][j] = 1
				else:
					self.mat[i][j] = 0

class Solution:
    """
    @param n: an integer
    @return: return an int
    """
    def lastFourDigitsOfFn(self, n):
        # write your code here
        if n == 0:
            return 0
        A = Matrix()
        A.mat = [[1, 1], [1, 0]]
        m = self.power(A, n - 1)
        return m.mat[0][0]
    
    def power(self, A, n):
        B = Matrix()
        B.unit()
        while n > 0:
            if n % 2 == 1:
                B = B * A
            A = A * A
            n = n // 2
        return B
