"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


class Solution:
    def isValid(self, s: str) -> bool:

        """
        This method will take in a string containing only  '(', ')', '{', '}', '[' and ']' and
        determines if the string is valid not

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

        :param s: String will only '(', ')', '{', '}', '[' and ']' characters
        :return: True if string is valid. Otherwise, False

        """
        val_par = []
        for each in list(s):
            try:
                if each in ['(', '{', '[']:
                    val_par.append(each)

                elif each == ')' and val_par[-1] == '(':
                    val_par.pop()

                elif each == '}' and val_par[-1] == '{':
                    val_par.pop()

                elif each == ']' and val_par[-1] == '[':
                    val_par.pop()

                else:
                    return False

            except IndexError:
                return False

        if len(val_par) == 0:
            return True
        else:
            return False