class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = [x_val for x_val in str(x)]
        return True if res == res[::-1] else False