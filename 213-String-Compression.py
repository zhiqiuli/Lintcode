class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        if not originalString:
            return ''
            
        res = []
        prev, count = None, 0
        for c in originalString:

            if not prev:
                prev = c

            if prev == c:
                count += 1

            if prev != c:
                res.append(prev)
                res.append(str(count))
                prev  = c
                count = 1

        res.append(prev)
        res.append(str(count))

        if len(originalString) <= len(res):
            return originalString
        else:
            return ''.join(res)
