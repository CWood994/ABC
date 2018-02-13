class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        _map = {}
        
        for n in nums:
            if n in _map:
                _map[n] += 1
            else:
                _map[n] = 1
                
        _max = -1
        ks = []
        
        for k,v in _map.items():
            if v > _max:
                _max = v
                ks = [k]
            elif v == _max:
                ks.append(k)
        
        _min = float('inf')
        print(ks)
        for k in ks:
            i1 = nums.index(k)
            i2 = len(nums) - 1 - nums[::-1].index(k)
            if (i2-i1+1) < _min:
                _min = i2-i1+1
                
        return _min
        