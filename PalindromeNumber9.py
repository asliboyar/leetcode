class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        reverse = 0
        while y > 0:
            remainder = y % 10
            y = y//10
            reverse = reverse * 10 + remainder
        return x == reverse
