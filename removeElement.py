"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code remove Element. 
 * the trick here is to keep in mind that you are working on a 
 * dynamic array an every time you delete and element the array size changes. 
 * Memory usage:16.33 MB.
 * time taken by the code to solve the problem: 45 ms.
 * Date: 2023-07-24.
 */

"""
from ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        list = nums[::]
        for x in list:
            if x == val:
                nums.remove(x)
        return len(nums)