class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return self.ispalindrome(s[left+1:right+1]) or self.ispalindrome(s[left:right])
            left  += 1
            right -= 1
        return True

    def ispalindrome(self, s):
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left  += 1
            right -= 1
        return True
