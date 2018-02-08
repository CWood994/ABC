class Solution:
    def findPairs(self, nums, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if target < 0:
            return 0
        
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        
        count = 0
        for k,v in map.items():
            if target == 0:
                if v >= 2:
                    count += 1
            else:
                if k + target in map:
                    count += 1
        return count