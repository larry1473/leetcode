class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            x =  s.find(i)
            y =  s.rfind(i)
            if  x == y:
                return x
        return -1 



        