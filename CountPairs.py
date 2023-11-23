"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code problem count pairs. 
 * Memory usage:16.22 MB.
 * time taken by the code to solve the problem: 78 ms.
 * Date: 2023-08-28.
 */

"""

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        p1 = 0 # first  pointer 
        p2 = p1 + 1 # second pointer 

        count = 0 # result keeper

        while p1 < len(nums):
            if(p2 >= len(nums)):
                p1 += 1
                p2 = 0
            elif(0 <= p1 < p2):
                if((nums[p1] + nums[p2]) < target ):
                    count += 1    
            p2 += 1
        return count 