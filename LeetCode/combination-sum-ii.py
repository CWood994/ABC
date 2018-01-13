class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        res = []
        self.dfs(candidates, res, [], 0, target)
        return res
    
    def dfs(self, nums, res, path, index, target):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return 
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
                
            self.dfs(nums, res, path+[nums[i]], i+1, target-nums[i])
            