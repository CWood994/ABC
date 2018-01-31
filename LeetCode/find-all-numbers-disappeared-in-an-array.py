class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        i = 0
        while i < len(nums):
            if nums[i] != i+1: 
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1],
                if nums[i] != nums[nums[i]-1]:
                    i -= 1
            i += 1
            
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
                
        return res
        