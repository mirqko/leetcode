"""
Given an integer array nums, return true if any value appears more than once 
in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

class Solution:
    def hasDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))

    nums_with_duplicate = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums_with_duplicate))