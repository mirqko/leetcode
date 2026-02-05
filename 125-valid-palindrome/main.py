"""
Given a string s, return true if it is a palindrome, or false otherwise.
A palindrome is a string that reads the same forward and backward after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.
Alphanumeric characters include letters and numbers.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2
Input: s = "race a car"
Output: false

Example 3:
Input: s = " "
Output: true
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_s = ''
        for char in s:
            if char.isalnum():
                alphanum_s += char.lower()
        if alphanum_s == alphanum_s[::-1]:
            return True
        else:
            return False