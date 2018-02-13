class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pos = 0
        res = []
        
        while pos < len(nums):
            if nums[pos] == pos+1:
                pos+=1
            elif nums[nums[pos]-1] == nums[pos]:
                res.append(nums[pos])
                pos += 1 
            else:
                nums[nums[pos]-1], nums[pos] = nums[pos], nums[nums[pos]-1]
        
        return list(set(res))
            
        