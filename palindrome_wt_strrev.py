
"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

This program uses String reversal technique to check for palindrome

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        """
        This method will take in an integer and
        returns a boolean value to represent whether it is an integer or not.
        This method uses String reversal technique to check for the palindrome

        :param x: number of type int to be checked of palindrome
        :return: True if x is palindrome. Otherwise, False

        """
        return str(x) == str(x)[::-1]