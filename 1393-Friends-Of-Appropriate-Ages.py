from typing import (
    List,
)

class Solution:
    """
    @param ages: 
    @return: 
    """
    def num_friend_requests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        age_to_count = collections.Counter(ages)
        res = 0
        for a in age_to_count:
            for b in age_to_count:
                if self.request(a, b):
                    if a != b:
                        res += age_to_count[a] * age_to_count[b]
                    else: # C(n, 2)
                        res += age_to_count[a] * (age_to_count[a] - 1)
        return res
    
    def request(self, a, b):
        return not ( b <= 0.5 * a + 7 or b > a or (b > 100 and a < 100) )
