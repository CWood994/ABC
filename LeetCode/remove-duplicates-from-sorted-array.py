class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1
        
        count = 1
        
        for i in range(1,len(nums)):
            if nums[count-1] != nums[i]:
                nums[count] = nums[i]
                count += 1
        
        return count
            
        