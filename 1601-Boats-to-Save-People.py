'''
双指针贪心算法。

如果最重的人可以与最轻的人共用一艘船，那么就这样做。
否则，最重的人不能与任何人配对，所以他们得到自己的船。

这样做的原因是因为如果最轻的人可以与任何人配对，他们也可以与最重的人配对。
让p[i]到目前最轻的人，让p[j]到最重的人。然后，如上所述，如果最重的人可以与最轻的人共享船（如果p[j] +p[i] <=限制），那么这样做;
否则，最重的人坐在自己的船上。
'''

from typing import (
    List,
)

class Solution:
    """
    @param people: The i-th person has weight people[i].
    @param limit: Each boat can carry a maximum weight of limit.
    @return: Return the minimum number of boats to carry every given person. 
    """
    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left, right = 0, len(people) - 1
        res = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left  += 1
                right -= 1
                res   += 1
            else:
                right -= 1
                res += 1
        return res
