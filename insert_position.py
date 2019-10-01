"""

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        This method will return the index of "target" in "nums" list.
        If "target" is not in the "nums" list then it will return the index
        where it can be inserted to preserve sorted order
        :param nums: list of integers
        :param target: integer to be searched in "nums" list
        :return: index of target if target in nums
                 index where it can be inserted if target not in nums
        """
        try:
            index = nums.index(target)
            return index
        except ValueError:
            i = 0
            while i < len(nums) and nums[i] < target:
                i = i + 1
            return i
        except TypeError:
            print('target and nums should be of type int ')


"""
Test Cases:
1.target is first element in the nums list
2.target is last element in the nums list
3.target is not present in the nums list and "can be inserted" position is index 0
4.target is not present in the nums list and "can be inserted" position is index = len(nums)
5.target variable type is not integer
6.nums list contains non integers
7.nums list has duplicates of target

"""