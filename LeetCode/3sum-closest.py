class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ns = sorted(nums)
        res = ns[0]+ns[1]+ns[2]
        
        for i in range(len(ns) - 2):
            j = i + 1
            k = len(ns) - 1

            while j < k:
                num = (ns[i]+ns[j]+ns[k])
                if abs(target-num) < abs(target-res):
                    res = num
                    
                if num < target:
                    j += 1
                else:
                    k -= 1
                    
        return res