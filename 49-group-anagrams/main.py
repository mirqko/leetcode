"""Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order. An anagram is a string that contains 
the exact same characters as another string, but the order of the characters can 
be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
"""

class Solution:
    def groupAnagrams(self, strs):
        anagrams_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            print(sorted_word)
            if not sorted_word in anagrams_dict:
                anagrams_dict[sorted_word] = []
            anagrams_dict[sorted_word].append(word)
        return [anagrams_dict[key] for key in anagrams_dict]
        