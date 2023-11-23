"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode  problem ArithmeticSubarray . 
 * Memory usage:13.78 MB.
 * time taken by the code to solve the problem: 135ms.
 * Date: 2023-11-23.
 */
"""

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        if(len(nums) == 0 or len(nums) == 1):
            return []
        index  = 0
        res  =  []
        while index < len(l):
            res.append(self.canBeArranged(nums[l[index]:r[index]+1]))
            index += 1
        return res 

    def canBeArranged(self,nums):
        new_nums = nums.sort()
        first_diff = 0
        second_diff = 0
        for i in range(len(nums)):
            if(i+1 < len(nums)):
                first_diff = nums[i] - nums[i+1]
                if(i == 0 ):
                    second_diff = first_diff 
                elif(second_diff != first_diff):
                    return False 
        return True 



        