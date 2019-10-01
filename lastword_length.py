"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        This method returns the length of the last word in a given string
        :param s: string to be checked for
        :return: the length of the last word in string "s"
        """
        return len(s.rstrip().split(' ')[-1])

"""
Test Cases
1. last word is of length > 1
2. last word is of length = 1
3. String s ends with multiple spaces
4. String s is empty
5. String s contains only spaces i.e "   "
6. String s contains multiple spaces of length > 1
"""