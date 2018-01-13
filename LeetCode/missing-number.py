class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            while(nums[i] != i):
                if nums[i] == len(nums):
                    break

                cur_val = nums[i]
                nums[i] = nums[nums[i]]
                nums[cur_val] = cur_val
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
            
        return len(nums)
    
    1,2
    
        