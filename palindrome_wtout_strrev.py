
"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

This program DOES NOT use String reversal technique to check for palindrome

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        """
        This method will take in an integer and
        returns a boolean value to represent whether it is an integer or not.
        This method DOES NOT use String reversal technique to check for the palindrome

        :param x: number of type int to be checked of palindrome
        :return: True if x is palindrome. Otherwise, False

        """

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            reverse_x = 0
            while x > reverse_x:
                reverse_x = (reverse_x*10) + (x % 10)
                x = int(x/10)

            if x == reverse_x or x == int(reverse_x/10):
                return True
            else:
                return False

