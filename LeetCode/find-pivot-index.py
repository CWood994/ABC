class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        
        right_sum = sum(nums)
        left_sum = 0
        prev = 0
        
        for i in range(len(nums)):
            left_sum += prev
            right_sum -= nums[i]
            prev = nums[i]
            if left_sum == right_sum :
                return i
            
        
        return -1