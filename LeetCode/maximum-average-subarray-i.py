class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        start = 0
        stop = k-1
        _sum = sum(nums[:k])
        _max = _sum
        
        while stop < len(nums)-1:
            _sum -= nums[start]
            start += 1
            stop += 1
            _sum += nums[stop]
            _max = max(_max, _sum)
        
        
        return _max/k
        