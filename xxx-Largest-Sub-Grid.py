# https://leetcode.com/discuss/interview-question/850974/hackerrank-online-assessment&#8205;&#8205;&#8205;&#8205;&#8204;&#8204;&#8204;&#8204;&#8204;&#8205;&#8204;&#8204;&#8204;&#8204;&#8205;&#8205;&#8204;&#8205;-roblox-new-grad-how-to-solve-this
'''
determine the max size of a square sub-grid such that all sub-grids of this size must have
sub-grid sum less than or equal to a given value (maxSum). Return the size of that sub-grid.

maxSum = 7
maxOfSubGridForSize_k = [0, 1, 4, 5, 10]
                        [y, y, y, y, n ] -> return 3

maxSum = 5
maxOfSubGridForSize_k = [0, 1, 4, 5, 10]
                        [y, y, y, y, n ] -> return 3
'''

from bisect import bisect_left, bisect_right
import sys

grid = [[2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]]

n = len(grid)
minSizeList = [0] * (n + 1)

# calculate the prefix sum
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + grid[i-1][j-1]

# calculate min for each k
for k in range(1, n + 1):
    min_val = -sys.maxsize
    for i in range(1 + (k - 1), n + 1):
        for j in range(1 + (k - 1), n + 1):
            min_val0 =   prefix_sum[i][j] \
                       - prefix_sum[i][j - 1 - (k - 1)] \
                       - prefix_sum[i - 1 - (k - 1)][j] \
                       + prefix_sum[i - 1 - (k - 1)][j - 1 - (k - 1)]
            min_val  = max(min_val, min_val0)
    minSizeList[k] = min_val
    

def bisect(left, right, nums, target):
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
    if nums[right] <= target: return right
    if nums[left]  <= target: return left
    return -1

res = bisect(0, len(minSizeList) - 1, minSizeList, 1)
print(res)

res = bisect(0, len(minSizeList) - 1, minSizeList, 13)
print(res)
res = bisect(0, len(minSizeList) - 1, minSizeList, 14)
print(res)
res = bisect(0, len(minSizeList) - 1, minSizeList, 15)
print(res)


res = bisect(0, len(minSizeList) - 1, minSizeList, 26)
print(res)
res = bisect(0, len(minSizeList) - 1, minSizeList, 27)
print(res)
res = bisect(0, len(minSizeList) - 1, minSizeList, 28)
print(res)

