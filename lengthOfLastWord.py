
"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode  problem length of the last word. 
 * the trick here is to keep in mind that you are working on a 
 * dynamic array an every time you delete and element the array size changes. 
 * Memory usage:17.14 MB.
 * time taken by the code to solve the problem: 68 ms.
 * Date: 2023-07-24.
 */

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split() # split the string using the spaces 
        return len(string[-1]) # gets the last element in the list and returns it's length