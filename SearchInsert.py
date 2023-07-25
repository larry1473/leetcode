
"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode  problem insert search . 
 * the trick here is to keep in mind that you are working on a 
 * dynamic array an every time you delete and element the array size changes. 
 * Memory usage:16.33 MB.
 * time taken by the code to solve the problem: 45 ms.
 * Date: 2023-07-24.
 */

"""
class Solution:

    def binaryInsert(self,nums, target: int, low:int, high:int) -> int:
        mid = low + (high - low)//2
        if high >= low and mid < len(nums):

            # If found at mid, then return it
            if nums[mid] == target:
                return mid

            # Search the left half
            elif nums[mid] > target:
                return self.binaryInsert(nums, target, low, mid-1)

            # Search the right half
            else:
                return self.binaryInsert(nums, target, mid + 1, high)

        else:
            return low

    def searchInsert(self, nums, target: int) -> int:
        return self.binaryInsert(nums,target,0,len(nums)-1)


