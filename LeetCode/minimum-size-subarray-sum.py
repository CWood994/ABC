class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        start = 0
        end = 0
        sumed = nums[0]
        _min = float("inf")
        
        while start < len(nums)-1:
            if sumed < s:
                end += 1
                if end >= len(nums):
                    break
                sumed += nums[end]
            elif sumed >= s:
                _min = min(_min, end-start+1)
                sumed -= nums[start]
                start += 1
                
        return _min if _min != float("inf") else 0
        
        
        