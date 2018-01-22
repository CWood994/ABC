class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        _max = _min = result = nums[0]
        
        for i in range(1, len(nums)):
            tmp = _max
            _max = max(_max * nums[i], _min * nums[i], nums[i])
            _min = min(tmp * nums[i], _min * nums[i], nums[i])
            if _max > result:
                result = _max
        
        return result