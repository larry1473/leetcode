class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dico = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if(s[i] in dico):
                if(dico[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in dico.values()):
                    return False
                dico[s[i]] = t[i]
        return True 

