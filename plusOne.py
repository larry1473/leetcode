
"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode problem plus one. 
 * Runtime : 18ms.
 * Memory usage:13.28 MB.
 * time taken by the code to solve the problem: 45 ms.
 * Date: 2023-07-24.
 */

"""
class Solution(object):
    def plusOne(self,digits):
       

        length = len(digits) - 1
        add = 1
        while(length >= 0):
            sum = digits[length] + 1
            if(sum < 10):
                digits[length] += 1
                return digits
            else:
                answer = digits[length] + add
                digits[length] = answer % 10
                add = answer // 10
            
                if(length == 0 and answer >= 10):
                    digits.insert(0,add)
                    return digits
                length -= 1
        return digits
        
        