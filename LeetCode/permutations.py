class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        self.helper(res, [], nums)
        return res
        
    def helper(self, ar, path, nums):
        if len(nums) == 0:
            ar.append(path)
            return
        
        for i in range(len(nums)):
            self.helper(ar, path+[nums[i]], nums[0:i]+nums[i+1:])
        