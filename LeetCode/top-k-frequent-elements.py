class Solution(object):
    def topKFrequent(self, nums, f):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not f:
            return []
        
        _map = {}
        
        for n in nums:
            if n in _map:
                _map[n] += 1
            else:
                _map[n] = 1
        
        buckets = [None] * (len(nums) + 1)
        
        for k,v in _map.items():
            if not buckets[v]:
                buckets[v] = [k]
            else:
                buckets[v].append(k)
                
        res = []
    
        for i in reversed(range(len(buckets))):
            if buckets[i]:
                while buckets[i] and f > 0:
                    res.append(buckets[i].pop())
                    f -= 1
            if f == 0:
                print("in")
    
        return res
        