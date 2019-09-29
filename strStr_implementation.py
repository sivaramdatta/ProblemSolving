"""

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        This method will return the index of the first occurrence of the needle
        inside the haystack string.
        :param haystack: String to search in
        :param needle: string to search for in haystack
        :return: index of the first occurrence of needle in haystack.
                -1 if needle is not available in haystack
                0 if needle is a blank string
        """
        if len(needle) == 0:
            return 0
        else:
            return haystack.find(needle)

"""

test cases

1. needle in haystack
2. needle not in haystack
3. multiple occurrences of needle in haystack
4. Haystack = empty string ""
5. needle = empty string ""
6. Haystack = integer
7. needle = integer
8. Haystack , needle = integer
9. len(needle) = len(haystack) 
10. needle length is longer than haystack

"""