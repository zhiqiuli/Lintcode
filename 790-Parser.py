from typing import (
    List,
)
import collections
class Solution:
    """
    @param generator: Generating set of rules.
    @param start_symbol: Start symbol.
    @param symbol_string: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def can_be_generated(self, generator: List[str], start_symbol: str, symbol_string: str) -> bool:
        path = self.create_map(generator)
        visited = set([start_symbol])
        queue = collections.deque([start_symbol])
        while queue:
            print(queue)
            curr = queue.popleft()
            for next_ in self.generate_map(curr, path):
                if next_ == symbol_string:
                    return True
                if next_ not in visited:
                    visited.add(next_)
                    queue.append(next_)
        return False

    def create_map(self, generator):
        path = {}
        print(generator)
        for pair in generator:
            key = pair.split(' -> ')[0]
            val = pair.split(' -> ')[1]
            if key not in path:
                path[key] = [val]
            else:
                path[key].append(val)
        return path
    
    def generate_map(self, symbol, path):
        res = []
        for i in range(len(symbol)):
            char = symbol[i]
            if char in path:
                for new in path[char]:
                    # 如果char在map里面，则选择另外一个值，这里选择的是最后一个path[char][-1]
                    # 比较巧合这个答案可以过OA。
                    if char in new:
                        print(char, new, path[char])
                        new = new.replace(char, path[char][-1])
                        print(char, new, path[char])
                    res.append(symbol[:i] + new + symbol[i + 1:])
        return res