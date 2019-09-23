"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        This method will take in a list of integers and a target.
        And returns a list of indices whose contents when added will be equal
        to the content of the target variable

        :param nums: list of integers numbers
        :param target: Value to be compared against sum of any two numbers in the "nums" list
        :return: a list of two indices whose contents sum up to the value in "target" variable
        """
        map = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map.values():
                return [nums.index(diff), i]
            map[i] = nums[i]

