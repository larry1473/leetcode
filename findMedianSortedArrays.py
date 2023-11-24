"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code problem find median Sorted arrays 
 * the trick was to merge the two arrays using the merge function from merge sort.
 * dynamic array an every time you delete and element the array size changes. 
 * Memory usage:13.58MB.
 * time taken by the code to solve the problem: 53 ms.
 * Date: 2023-07-24.
 */

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined_array = self.merge(nums1,nums2)
        median = self.findMedian(combined_array)
        return median
    
    def findMedian (self,nums):
        if(len(nums) % 2 != 0):
            mid = len(nums)//2
            return float(nums[mid])
        else:
            mid = len(nums)//2
            mid_pred  = mid - 1 
            if( mid_pred >= 0):
                res = ( float(nums[mid])+  float(nums[mid_pred]) ) / 2
                return res  
            else:
                return 0

    def merge(self, left,right):
        result = []
        left_idx = 0 
        right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        return result

        