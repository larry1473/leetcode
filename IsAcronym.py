"""
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode  problem isAcronym . 
 * Memory usage:16.07 MB.
 * time taken by the code to solve the problem: 63 ms.
 * Date: 2023-08-28.
 */
"""
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = ""
        for x in range(len(words)):
            res += words[x][0]
        return res == s