class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def is_number(self, s: str) -> bool:

        s = s.strip()
        if not s:
            return False

        decimal = False
        plus    = False
        minus   = False
        exp     = False
        for i in range(len(s)):
            if s[i].isdigit():
                continue

            elif s[i] == '+':
                if plus:
                    return False
                if i != 0:
                    return False
                plus = True

            elif s[i] == '-':
                if minus:
                    return False
                if i != 0:
                    return False
                minus = True
            
            elif s[i] == '.':
                if decimal:
                    return False
                if i == 0 and len(s) == 1:
                    return False
                decimal = True
            
            elif s[i] == 'e':
                if exp:
                    return False
                if i == 0 or i == len(s) - 1:
                    return False
                exp = True
            
            else:
                return False
        
        return True
