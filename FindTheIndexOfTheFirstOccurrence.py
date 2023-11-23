"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code problem find the index of the first occurrence of a string in a string. 
 * the trick here is to keep in mind that you are working on a 
 * dynamic array an every time you delete and element the array size changes. 
 * Memory usage:16.33 MB.
 * time taken by the code to solve the problem: 48 ms.
 * Date: 2023-07-24.
 */

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return -1 if not (needle in haystack) else haystack.index(needle)