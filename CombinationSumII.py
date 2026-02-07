class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def combination(curr, start, target):
            if target == 0:
                res.append(curr)
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue # avoid duplicate solutions 
                if candidates[i] > target:
                    break
                combination(curr + [candidates[i]], i+1, target - candidates[i])
            return 
        combination([],0,target)
        return res 