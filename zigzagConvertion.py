class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ["" for _ in range(numRows)]

        index  = 0
        direction = -1
        for c in s:
            res[index] += c
            if index == 0 or (index == numRows - 1):
                direction = - direction 
            index += direction 
        return "".join(res)