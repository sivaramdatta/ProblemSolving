"""
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer

"""



class Solution:
    def reverse(self, x: int) -> int:

        """
        This method takes in an int number and reverses the digits in that number.
        If the reversed integer is in the range of 32-bit signed int then it will be returned.
        Otherwise, 0 will be returned

        :param x: Integer that needs to be reversed
        :return: reversed 32 bit signed integer

        """
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)