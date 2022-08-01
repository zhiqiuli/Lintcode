class Solution:
    """
    @param str: String
    @return: String
    """
    def shortest_palindrome(self, str: str) -> str:
        # Write your code here
        for i in range(len(str)):
            if self.is_palindrome(str[:len(str) - i]):
                return str[len(str) - i:][::-1] + str
        return ''

    def is_palindrome(self, string):
        start, end = 0, len(string) - 1
        while start <= end:
            if string[start] != string[end]:
                return False
            else:
                start += 1
                end -= 1
        return True