"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode problem remove duplicate . 
 * Memory usage:18 MB.
 * time taken by the code to solve the problem: 107 ms.
 * Date: 2023-07-24.
 */

"""

from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        back = 1 
        front = back 
        
        while front < len(nums):
            if(nums[front] - nums[front - 1] != 0 ):
                nums[back] = nums[front]
                back += 1
            front += 1
        return back 