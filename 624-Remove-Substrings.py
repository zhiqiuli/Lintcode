class Solution:
    """
    @param s: a string
    @param dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        seen = set([s])
        queue = collections.deque([s])
        min_len = len(s)
        while queue:
            string = queue.popleft()
            for substr in dict:
                found = string.find(substr)
                while found != -1:
                    new_string = string[:found] + string[found+len(substr):]
                    if new_string not in seen:
                        seen.add(new_string)
                        queue.append(new_string)
                        min_len = min(min_len, len(new_string))
                    found = string.find(substr, found+1)
        return min_len
