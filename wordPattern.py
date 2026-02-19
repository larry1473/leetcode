class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        dico = {}
        if len(pattern) != len(arr):
            return False
        for i, char in enumerate(pattern):
            if char not in dico:
                if(arr[i] in dico.values()):
                    return False
                dico[char] = arr[i]
            else:
                if(dico[char] != arr[i]):
                    return False 
        return True 