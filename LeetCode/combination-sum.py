class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(res, [], candidates, 0, target)
        return res
    
    def dfs(self, res, path, candidates, index, target):
        if target == 0:
            res.append(path)
        if target < 0:
            return
        for i in range(index, len(candidates)):
            self.dfs(res, path+[candidates[i]], candidates, i, target - candidates[i])
                    
        