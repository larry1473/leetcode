class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res 
        res.append([1,1])
        if numRows == 2:
            return res 
        extend = numRows - 2
        for i in range(extend):
            res.append(self._helper(res[-1]))
        return res 
    
    def _helper (self, arr):
        new_arr = arr
        res = [1,1]
        index = 0
        while index < len(arr):
            if(index + 1 < len(arr)):
                res.insert(1,arr[index] + arr[index + 1])
            index += 1
        return res 